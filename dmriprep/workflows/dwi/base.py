# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# Copyright 2021 The NiPreps Developers <nipreps@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
"""Orchestrating the dMRI-preprocessing workflow."""
from pathlib import Path

from dmriprep.interfaces import DerivativesDataSink
from dmriprep.interfaces.reports import DWISummary
from dmriprep.workflows.dwi.post_sdc.epi_reg.epi_reg import init_epireg_wf
from dmriprep.workflows.dwi.utils import _aslist, _get_wf_name
from nipype.interfaces import utility as niu
from nipype.pipeline import engine as pe

from ... import config
from .outputs import init_reportlets_wf


def init_dwi_preproc_wf(dwi_file):
    """
    Build a preprocessing workflow for one DWI run.

    Workflow Graph
        .. workflow::
            :graph2use: orig
            :simple_form: yes

            from dmriprep.config.testing import mock_config
            from dmriprep import config
            from dmriprep.workflows.dwi.base import init_dwi_preproc_wf
            with mock_config():
                wf = init_dwi_preproc_wf(
                    f"{config.execution.layout.root}/"
                    "sub-THP0005/dwi/sub-THP0005_dwi.nii.gz"
                )

    Parameters
    ----------
    dwi_file : :obj:`os.PathLike`
        One diffusion MRI dataset to be processed.
    has_fieldmap : :obj:`bool`
        Build the workflow with a path to register a fieldmap to the DWI.

    Inputs
    ------
    dwi_file
        dwi NIfTI file
    in_bvec
        File path of the b-vectors
    in_bval
        File path of the b-values
    fmap
        File path of the fieldmap
    fmap_ref
        File path of the fieldmap reference
    fmap_coeff
        File path of the fieldmap coefficients
    fmap_mask
        File path of the fieldmap mask
    fmap_id
        The BIDS modality label of the fieldmap being used

    Outputs
    -------
    dwi_reference
        A 3D :math:`b = 0` reference, before susceptibility distortion correction.
    dwi_mask
        A 3D, binary mask of the ``dwi_reference`` above.
    gradients_rasb
        A *RASb* (RAS+ coordinates, scaled b-values, normalized b-vectors, BIDS-compatible)
        gradient table.

    See Also
    --------
    * :py:func:`~dmriprep.workflows.dwi.outputs.init_dwi_derivatives_wf`
    * :py:func:`~dmriprep.workflows.dwi.outputs.init_reportlets_wf`

    """
    from dmriprep.workflows.dwi.conversions.nii_to_mif.nii_to_mif_wf import (
        init_nii_to_mif_wf,
    )
    from dmriprep.workflows.dwi.fieldmap_query.fieldmap_query import (
        init_fieldmap_query,
    )
    from dmriprep.workflows.dwi.fieldmap_query.nodes import (
        is_same_size,
        locate_opposite_phase,
    )
    from dmriprep.workflows.dwi.post_sdc.post_sdc import init_post_sdc_wf
    from dmriprep.workflows.dwi.pre_sdc.pre_sdc import init_pre_sdc_wf
    from dmriprep.workflows.dwi.sdc.sdc import init_sdc_wf
    from dmriprep.workflows.dwi.utils.outputs.derivatives.derivatives import (
        init_derivatives_wf,
    )
    from niworkflows.engine.workflows import LiterateWorkflow as Workflow
    from niworkflows.interfaces.nibabel import ApplyMask

    dwi_file = Path(dwi_file)
    config.loggers.workflow.debug(
        f"Creating DWI preprocessing workflow for <{dwi_file.name}>"
    )

    # Build workflow
    workflow = Workflow(name=_get_wf_name(dwi_file.name))

    inputnode = pe.Node(
        niu.IdentityInterface(
            fields=[
                # DWI
                "dwi_file",
                # fmap
                "fmap_file",
                # From anatomical
                "t1w_preproc",
                "t1w_mask",
                "t1w_dseg",
                "t1w_aseg",
                "t1w_aparc",
                "t1w_tpms",
                "template",
                "anat2std_xfm",
                "std2anat_xfm",
                "subjects_dir",
                "subject_id",
                "t1w2fsnative_xfm",
                "fsnative2t1w_xfm",
            ]
        ),
        name="inputnode",
    )
    inputnode.inputs.dwi_file = str(dwi_file.absolute())
    fmap, is_dwi, pe_dir = locate_opposite_phase(str(dwi_file.absolute()))
    seepi = is_same_size(fmap, str(dwi_file.absolute()))
    inputnode.inputs.fmap_file = fmap
    # fmap_query = init_fieldmap_query()
    # workflow.connect([(inputnode, fmap_query, [("dwi_file", "dwi_file")])])
    mif_conversion_wf = init_nii_to_mif_wf()
    pre_sdc_wf = init_pre_sdc_wf()
    workflow.connect(
        [
            (
                inputnode,
                mif_conversion_wf,
                [
                    ("dwi_file", "inputnode.dwi_file"),
                    ("fmap_file", "inputnode.fmap_file"),
                ],
            ),
            # (
            #     fmap_query,
            #     mif_conversion_wf,
            #     [("fmap_file", "inputnode.fmap_file")],
            # ),
            (
                mif_conversion_wf,
                pre_sdc_wf,
                [
                    ("outputnode.dwi_file", "inputnode.dwi_file"),
                ],
            ),
        ]
    )
    sdc_wf = init_sdc_wf(seepi)
    ds_report_eddy = pe.Node(
        DerivativesDataSink(
            base_directory=str(config.execution.output_dir),
            desc="eddy",
            datatype="figures",
        ),
        name="ds_report_eddy",
        run_without_submitting=True,
    )
    sdc_wf.inputs.inputnode.dwi_pe_dir = pe_dir
    workflow.connect(
        [
            (
                pre_sdc_wf,
                sdc_wf,
                [
                    ("outputnode.dwi_pre_sdc", "inputnode.dwi_file"),
                    ("outputnode.mean_bzero", "inputnode.mean_bzero"),
                    ("outputnode.bzero", "inputnode.dwi_bzero"),
                ],
            ),
            # (
            #     fmap_query,
            #     sdc_wf,
            #     [
            #         ("dwi_pe_dir", "inputnode.dwi_pe_dir"),
            #     ],
            # ),
            (
                mif_conversion_wf,
                sdc_wf,
                [("outputnode.fmap_file", "inputnode.fmap_file")],
            ),
            (inputnode, ds_report_eddy, [("dwi_file", "source_file")]),
            (sdc_wf, ds_report_eddy, [("eddy_report.out_report", "in_file")]),
        ]
    )

    t1w_brain = pe.Node(ApplyMask(), name="t1w_brain")
    workflow.connect(
        [
            (
                inputnode,
                t1w_brain,
                [("t1w_preproc", "in_file"), ("t1w_mask", "in_mask")],
            ),
        ]
    )
    post_sdc_wf = init_post_sdc_wf()
    workflow.connect(
        [
            (
                sdc_wf,
                post_sdc_wf,
                [("outputnode.dwi_preproc", "inputnode.dwi_file")],
            ),
        ]
    )
    epi_reg_wf = init_epireg_wf()
    workflow.connect(
        [
            (
                post_sdc_wf,
                epi_reg_wf,
                [
                    ("outputnode.mean_bzero", "inputnode.dwi_reference"),
                    ("outputnode.dwi_mif", "inputnode.dwi_file"),
                ],
            ),
            (
                inputnode,
                epi_reg_wf,
                [
                    ("t1w_preproc", "inputnode.t1w_head"),
                    ("t1w_mask", "inputnode.t1w_mask"),
                ],
            ),
            (t1w_brain, epi_reg_wf, [("out_file", "inputnode.t1w_brain")]),
        ]
    )
    derivatives_wf = init_derivatives_wf()
    derivatives_wf.inputs.inputnode.set(
        base_directory=config.execution.output_dir
    )
    workflow.connect(
        [
            (
                inputnode,
                derivatives_wf,
                [("dwi_file", "inputnode.source_file")],
            ),
            (
                post_sdc_wf,
                derivatives_wf,
                [
                    (
                        "dwi_conversion_node.out_file",
                        "inputnode.native_dwi_file",
                    ),
                    (
                        "dwi_conversion_node.json_export",
                        "inputnode.native_dwi_json",
                    ),
                    (
                        "dwi_conversion_node.out_bvec",
                        "inputnode.native_dwi_bvec",
                    ),
                    (
                        "dwi_conversion_node.out_bval",
                        "inputnode.native_dwi_bval",
                    ),
                    (
                        "dwi_conversion_node.out_grad_mrtrix",
                        "inputnode.native_dwi_grad",
                    ),
                    (
                        "extract_bzero.outputnode.bzero_json",
                        "inputnode.native_dwiref_json",
                    ),
                    (
                        "extract_bzero.outputnode.bzero_json",
                        "inputnode.coreg_dwiref_json",
                    ),
                    (
                        "extract_bzero.outputnode.mean_bzero",
                        "inputnode.native_dwiref_file",
                    ),
                ],
            ),
            (
                epi_reg_wf,
                derivatives_wf,
                [
                    (
                        "dwi_conversion_node.out_file",
                        "inputnode.coreg_dwi_file",
                    ),
                    (
                        "dwi_conversion_node.json_export",
                        "inputnode.coreg_dwi_json",
                    ),
                    (
                        "dwi_conversion_node.out_bvec",
                        "inputnode.coreg_dwi_bvec",
                    ),
                    (
                        "dwi_conversion_node.out_bval",
                        "inputnode.coreg_dwi_bval",
                    ),
                    (
                        "dwi_conversion_node.out_grad_mrtrix",
                        "inputnode.coreg_dwi_grad",
                    ),
                    (
                        "outputnode.dwi_ref_to_t1w",
                        "inputnode.coreg_dwiref_file",
                    ),
                    (
                        "outputnode.native_dwi_mask",
                        "inputnode.native_dwi_mask",
                    ),
                    ("outputnode.epi_to_t1w_aff", "inputnode.epi_to_t1w_aff"),
                    ("outputnode.t1w_to_epi_aff", "inputnode.t1w_to_epi_aff"),
                    ("outputnode.coreg_dwi_mask", "inputnode.coreg_dwi_mask"),
                ],
            ),
        ]
    )
    reportlets_wf = init_reportlets_wf(
        str(config.execution.output_dir),
        sdc_report=True,
    )
    workflow.connect(
        [
            (
                inputnode,
                reportlets_wf,
                [
                    ("dwi_file", "inputnode.source_file"),
                    ("t1w_preproc", "inputnode.t1w_head"),
                ],
            ),
            (
                post_sdc_wf,
                reportlets_wf,
                [
                    (
                        "extract_bzero.outputnode.mean_bzero",
                        "inputnode.dwi_ref",
                    ),
                ],
            ),
            (
                epi_reg_wf,
                reportlets_wf,
                [
                    ("outputnode.native_dwi_mask", "inputnode.dwi_mask"),
                    ("outputnode.dwi_ref_to_t1w", "inputnode.coreg_dwi_ref"),
                ],
            ),
            (
                sdc_wf,
                reportlets_wf,
                [("eddy_report.out_report", "inputnode.sdc_report")],
            ),
        ]
    )
    summary = pe.Node(
        DWISummary(
            distortion_correction="PEPOLAR",
            pe_direction="j-",
            registration="FSL",
            registration_dof=6,
            fallback=False,
        ),
        name="DWI_summary",
        run_without_submitting=True,
    )
    ds_report_summary = pe.Node(
        DerivativesDataSink(
            base_directory=str(config.execution.output_dir),
            desc="dwi_summary",
            datatype="figures",
        ),
        name="ds_report_summary",
        run_without_submitting=True,
    )
    workflow.connect(
        [
            (summary, ds_report_summary, [("out_report", "in_file")]),
            (inputnode, ds_report_summary, [("dwi_file", "source_file")]),
        ]
    )
    return workflow
