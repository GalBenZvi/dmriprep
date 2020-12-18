Search.setIndex({docnames:["api","api/dmriprep.config","api/dmriprep.interfaces","api/dmriprep.interfaces.images","api/dmriprep.interfaces.reports","api/dmriprep.interfaces.vectors","api/dmriprep.utils","api/dmriprep.utils.bids","api/dmriprep.utils.images","api/dmriprep.utils.misc","api/dmriprep.utils.vectors","api/dmriprep.workflows","api/dmriprep.workflows.base","api/dmriprep.workflows.dwi","api/dmriprep.workflows.dwi.base","api/dmriprep.workflows.dwi.outputs","api/dmriprep.workflows.dwi.util","api/dmriprep.workflows.fmap","api/dmriprep.workflows.fmap.base","changes","index","installation","links","roadmap","usage"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.index":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,sphinx:56},filenames:["api.rst","api/dmriprep.config.rst","api/dmriprep.interfaces.rst","api/dmriprep.interfaces.images.rst","api/dmriprep.interfaces.reports.rst","api/dmriprep.interfaces.vectors.rst","api/dmriprep.utils.rst","api/dmriprep.utils.bids.rst","api/dmriprep.utils.images.rst","api/dmriprep.utils.misc.rst","api/dmriprep.utils.vectors.rst","api/dmriprep.workflows.rst","api/dmriprep.workflows.base.rst","api/dmriprep.workflows.dwi.rst","api/dmriprep.workflows.dwi.base.rst","api/dmriprep.workflows.dwi.outputs.rst","api/dmriprep.workflows.dwi.util.rst","api/dmriprep.workflows.fmap.rst","api/dmriprep.workflows.fmap.base.rst","changes.rst","index.rst","installation.rst","links.rst","roadmap.rst","usage.rst"],objects:{"dmriprep.config":{dumps:[1,1,1,""],environment:[1,2,1,""],execution:[1,2,1,""],from_dict:[1,1,1,""],get:[1,1,1,""],init_spaces:[1,1,1,""],load:[1,1,1,""],loggers:[1,2,1,""],nipype:[1,2,1,""],redirect_warnings:[1,1,1,""],to_filename:[1,1,1,""],workflow:[1,2,1,""]},"dmriprep.config.environment":{cpu_count:[1,3,1,""],exec_docker_version:[1,3,1,""],exec_env:[1,3,1,""],free_mem:[1,3,1,""],nipype_version:[1,3,1,""],overcommit_limit:[1,3,1,""],overcommit_policy:[1,3,1,""],templateflow_version:[1,3,1,""],version:[1,3,1,""]},"dmriprep.config.execution":{anat_derivatives:[1,3,1,""],bids_description_hash:[1,3,1,""],bids_dir:[1,3,1,""],bids_filters:[1,3,1,""],boilerplate_only:[1,3,1,""],debug:[1,3,1,""],fs_license_file:[1,3,1,""],fs_subjects_dir:[1,3,1,""],init:[1,4,1,""],layout:[1,3,1,""],log_dir:[1,3,1,""],log_level:[1,3,1,""],low_mem:[1,3,1,""],md_only_boilerplate:[1,3,1,""],notrack:[1,3,1,""],output_dir:[1,3,1,""],output_spaces:[1,3,1,""],participant_label:[1,3,1,""],reports_only:[1,3,1,""],run_uuid:[1,3,1,""],templateflow_home:[1,3,1,""],work_dir:[1,3,1,""],write_graph:[1,3,1,""]},"dmriprep.config.loggers":{"default":[1,3,1,""],"interface":[1,3,1,""],cli:[1,3,1,""],init:[1,4,1,""],utils:[1,3,1,""],workflow:[1,3,1,""]},"dmriprep.config.nipype":{crashfile_format:[1,3,1,""],get_linked_libs:[1,3,1,""],get_plugin:[1,4,1,""],init:[1,4,1,""],memory_gb:[1,3,1,""],nprocs:[1,3,1,""],omp_nthreads:[1,3,1,""],parameterize_dirs:[1,3,1,""],plugin:[1,3,1,""],plugin_args:[1,3,1,""],resource_monitor:[1,3,1,""],stop_on_first_crash:[1,3,1,""]},"dmriprep.config.workflow":{anat_only:[1,3,1,""],dwi2t1w_init:[1,3,1,""],fmap_bspline:[1,3,1,""],fmap_demean:[1,3,1,""],force_syn:[1,3,1,""],hires:[1,3,1,""],ignore:[1,3,1,""],longitudinal:[1,3,1,""],run_reconall:[1,3,1,""],skull_strip_fixed_seed:[1,3,1,""],skull_strip_template:[1,3,1,""],spaces:[1,3,1,""],use_syn:[1,3,1,""]},"dmriprep.interfaces":{BIDSDataGrabber:[2,2,1,""],DerivativesDataSink:[2,2,1,""],images:[3,0,0,"-"],reports:[4,0,0,"-"],vectors:[5,0,0,"-"]},"dmriprep.interfaces.DerivativesDataSink":{out_path_base:[2,3,1,""]},"dmriprep.interfaces.images":{ExtractB0:[3,2,1,""],RescaleB0:[3,2,1,""]},"dmriprep.interfaces.reports":{AboutSummary:[4,2,1,""],SubjectSummary:[4,2,1,""],SummaryInterface:[4,2,1,""]},"dmriprep.interfaces.vectors":{CheckGradientTable:[5,2,1,""]},"dmriprep.utils":{bids:[7,0,0,"-"],images:[8,0,0,"-"],misc:[9,0,0,"-"],vectors:[10,0,0,"-"]},"dmriprep.utils.bids":{collect_data:[7,1,1,""],validate_input_dir:[7,1,1,""],write_derivative_description:[7,1,1,""]},"dmriprep.utils.images":{extract_b0:[8,1,1,""],median:[8,1,1,""],rescale_b0:[8,1,1,""]},"dmriprep.utils.misc":{check_deps:[9,1,1,""],sub_prefix:[9,1,1,""]},"dmriprep.utils.vectors":{DiffusionGradientTable:[10,2,1,""],b0mask_from_data:[10,1,1,""],bvecs2ras:[10,1,1,""],calculate_pole:[10,1,1,""],normalize_gradients:[10,1,1,""],rasb_dwi_length_check:[10,1,1,""]},"dmriprep.utils.vectors.DiffusionGradientTable":{affine:[10,4,1,""],b0mask:[10,4,1,""],bvals:[10,4,1,""],bvecs:[10,4,1,""],generate_rasb:[10,4,1,""],generate_vecval:[10,4,1,""],gradients:[10,4,1,""],normalize:[10,4,1,""],normalized:[10,4,1,""],pole:[10,4,1,""],reorient_rasb:[10,4,1,""],to_filename:[10,4,1,""]},"dmriprep.workflows":{base:[12,0,0,"-"],dwi:[13,0,0,"-"]},"dmriprep.workflows.base":{init_dmriprep_wf:[12,1,1,""],init_single_subject_wf:[12,1,1,""]},"dmriprep.workflows.dwi":{base:[14,0,0,"-"],outputs:[15,0,0,"-"],util:[16,0,0,"-"]},"dmriprep.workflows.dwi.base":{init_dwi_preproc_wf:[14,1,1,""]},"dmriprep.workflows.dwi.outputs":{init_reportlets_wf:[15,1,1,""]},"dmriprep.workflows.dwi.util":{init_dwi_reference_wf:[16,1,1,""],init_enhance_and_skullstrip_dwi_wf:[16,1,1,""]},dmriprep:{config:[1,0,0,"-"],interfaces:[2,0,0,"-"],utils:[6,0,0,"-"],workflows:[11,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","attribute","Python attribute"],"4":["py","method","Python method"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:attribute","4":"py:method"},terms:{"02deb54a823f":1,"121754_aa0b4fa9":1,"142435_0cb37202":1,"1a0":20,"1st":20,"27121_a22e51b47c544980bad594d5e0bb2d04":10,"3dautomask":16,"3dshore":23,"3dunif":16,"4a11":1,"4aac":1,"6b60":1,"6mm":16,"boolean":[2,5],"case":[23,24],"class":[0,1,2,3,4,5,10],"default":[1,2,5,16,24],"export":1,"final":16,"float":[3,5,10],"function":[0,1,2,21,23],"import":[1,24],"int":[10,16],"long":[19,20],"new":[1,20,21],"return":10,"static":10,"switch":1,"true":[1,2,5,7,10],"try":21,ARS:10,Added:19,Adding:19,B0s:3,For:[20,21,24],LAS:10,LPS:10,NOT:24,One:[3,14],RAS:[10,14],The:[1,2,10,14,16,19,20,21],Then:16,There:21,These:21,Use:[19,24],Using:23,_config:1,abl:24,aboout:23,about:[12,19,23],aboutsummari:4,abov:[14,21,23],absenc:1,access:[1,24],accord:19,acquisit:[10,20],across:[1,8,20,24],action:[1,19],ad2b8baf09f6:1,adam:19,adapt:[16,20,23],add:[1,19],addict:19,addit:[21,24],address:[19,20],adher:[19,20,21],adopt:19,advanc:20,af7d:1,affili:19,affin:[10,16],afni:[16,21],afq:19,after:[1,16,19,21,23],aggreg:24,agnost:20,ahead:21,aka:19,algorithm:16,all:[1,3,10,12,19,20,21,24],allclos:5,alloc:1,allow:[1,19,21],allowed_ent:2,alpha:23,also:[19,20,21,23],altern:[1,21,24],although:24,amazonaw:10,ambiti:21,amd64:21,amount:19,amplitud:10,analysi:[20,23],analysis_level:[21,24],analyt:[1,20],analyz:23,anat:24,anat_deriv:1,anat_onli:1,anatom:[1,12,19,24],ani:[1,2,12,20,24],anisha:19,anoth:24,answer:20,ant:[16,20,21],antsbrainextract:24,anyon:19,api:20,app:[21,24],appear:21,appli:16,applic:[16,20],approach:[21,23],april:20,arg:[1,2],argument:[1,20,21],ariel:19,around:23,arrai:10,artifact:23,ask:20,aspect:24,assess:24,assum:24,attempt:[19,24],austin:19,autom:[1,21],automat:20,avail:[1,16,20,21,24],averag:[3,8,10,23],b07ee615a588acf67967d70f5b2402ffbe477b99a316433fa7fdaff4f9dad5c1:1,b0_ix:[3,5,8,16],b0_threshold:[5,10],b0mask:10,b0mask_from_data:10,b0s:[3,16],b9fd:1,b_scale:[5,10],back:19,bare:21,base:[0,1,2,3,4,5,10,11,13,17,20,21,23],base_directori:2,bash:21,basi:1,basic:20,batteri:[15,19],bbregist:19,becom:20,been:10,befor:[14,20],begin:20,behavior:19,being:14,below:[10,19],best:20,bet:16,better:20,between:23,bia:[16,23],bias_corrected_fil:16,bid:[0,1,2,6,14,20,21,23],bids_description_hash:1,bids_dir:[1,7,24],bids_filt:1,bids_root:24,bids_valid:7,bidsdatagrabb:2,bidslayout:1,big:19,binari:[14,21],blob:24,board:20,boilerpl:[1,24],boilerplate_onli:[1,24],bold:2,bool:14,bound:24,brain:[1,16,20],brainmask:19,branch:19,breed:20,bring:19,broken:19,bspline:24,bugfix:19,build:[1,14,16,19,20,21],build_workflow:1,built:1,bval:[5,10],bvec:[5,10],bvec_norm_epsilon:[5,10],bvecs2ra:10,c3d:21,cach:1,calcul:[10,16,23,24],calculate_pol:10,call:[1,10,24],can:[1,19,20,21,23,24],candid:23,capabl:[19,21],categori:1,center:24,centr:19,chacon:20,challeng:20,chang:[1,19,20],changelog:19,chapter:20,charact:1,chdir:[3,5],check:[5,10,19,21,24],check_dep:9,check_hdr:2,checkgradientt:5,checkout:21,checkpoint:1,checksum:1,choic:24,chose:21,cieslak:19,circleci:19,citat:24,citi:24,classmethod:1,clean:[20,24],cleanenv:24,clear:24,cli:[1,24],client:[1,21],cloud:20,code:[1,12,14,16,19,20],coeffici:14,coerc:2,cohort:24,collect:[1,12],collect_data:7,colon:24,com:[10,21,24],come:21,command:[1,4,19,20,21],commerci:20,commit:19,common:24,commun:23,compar:21,compat:14,complet:24,complex:20,compliant:[1,24],compos:[10,21],comprehend:12,compress:2,comput:[1,24],concern:20,concurr:24,conduct:20,config:[0,19,20,24],config_fil:1,configur:[0,20,21],consid:[10,23],consist:1,consumpt:1,contact:21,contain:[1,2,4,20,23,24],container_command_and_opt:21,container_imag:21,content:[19,24],continu:[1,19],contrast:16,contribut:[19,20],contributor:[19,20],conveni:1,convers:[1,10],convert:[1,10],coordin:[10,14],copi:1,core:[2,3,4,5],coregist:24,coregistr:1,correct:[5,14,16,20,23],correctli:21,correspond:[1,10,24],count:19,countri:24,cover:10,cpu:[1,24],cpu_count:1,crash:24,crashfil:1,crashfile_format:1,crawl:1,creat:[1,12,20,21],crucial:24,current:[1,20,21,23],custom:[2,16,19,24],d14f:1,daemon:21,data:[1,2,10,16,19,20,23,24],data_dir:[3,5],data_dtyp:2,datalad:19,dataset:[1,8,10,14,16,19,20,23,24],dataset_descript:1,datasink:[2,15],datatyp:2,deal:3,debian:21,debug:[1,24],decai:3,decemb:20,defin:24,definit:24,delet:19,delimit:24,demean:24,denois:23,dep:19,depart:19,depend:[9,19,20,24],deploi:[19,21],deploy:19,derek:19,deriv:[1,2,12,15,19,20,23,24],deriv_dir:7,derivatives_path:21,derivativesdatasink:[2,19],describ:[19,24],descript:[1,21],design:[1,20,24],detail:24,develop:[19,20,24],dicki:19,dict:1,dictionari:[1,2],diffus:[10,12,14,20,23,24],diffusiongradientt:[10,19],dilat:16,dimens:8,dipi:23,dir:24,direct:12,directori:[1,2,4,24],disabl:24,disk:[1,24],dismiss_ent:2,displac:23,distort:[1,14,20,23],distribut:16,dmri:[14,20,23,24],dmriprep:[0,21,24],dmriprep_named_opt:21,doc:[19,21],docker:[1,19,20,24],dockerfil:[19,21],dockerout:24,document:[19,20,21],doe:[1,24],doing:23,don:24,done:24,drift:[3,23],driven:[10,19],drop:21,ds001771:19,dtype:[2,19],dump:1,dwi2t1w:24,dwi2t1w_init:1,dwi:[0,1,2,3,4,5,8,10,11,12,19,24],dwi_fil:[5,10,14,16],dwi_mask:[3,14,16],dwi_refer:14,dwi_reference_wf:16,each:[1,12,16,20,24],earli:[1,23],earlier:23,easi:20,easili:[1,20],eddi:[20,23],edu:24,effect:24,either:[1,24],element:16,email:20,enabl:[1,24],encod:10,encompass:20,engin:[1,21],enh:19,enhanc:16,enhance_and_skullstrip_dwi_wf:16,enlist:1,ensur:[5,20,24],entiti:[2,12,24],environ:[1,20,24],equip:20,error:[1,19,24],escienc:19,esteban:19,estim:[1,3,10,19,23],etc:[1,20],evalu:[10,23],even:24,event:24,everi:1,exact:24,exampl:[1,3,5,9,10,20,21,24],exclus:[5,23],exec_docker_vers:1,exec_env:[1,7],execut:[1,12,19,20,21],exercis:19,exist:[1,2,3,4,5,24],exit:24,expect:23,experiment:24,explain:20,explor:23,extern:20,extra:21,extract:[1,2,3,8,16,23],extract_b0:[3,8],extractb0:3,eye:10,fact:[19,24],factor:3,fair:19,fals:[1,2,10,14,15],familiar:20,fast:[1,19],favour:19,feel:20,field:[1,16,23,24],fieldmap:[1,2,14,20],figure1:19,file:[1,2,3,4,5,10,14,16,19,21,24],filenam:[1,10],filesystem:1,filetyp:10,filter:[1,20],find:20,first:[1,19,21,24],fit:[20,24],fix:[1,2,19,24],fixed_hdr:2,flag:[1,24],flair:2,flake8:19,flat:1,flexibl:19,flow:20,flowchart:19,fmap:[0,2,11,14,24],fmap_bsplin:1,fmap_coeff:14,fmap_demean:1,fmap_id:14,fmap_mask:14,fmap_ref:14,fmriprep:[19,24],folder:[1,12,24],follow:[19,21,23,24],forc:24,force_syn:1,forkserv:1,form:[5,24],format:[1,20],found:[1,19,21,24],frame:10,framewis:23,framework:21,free:[1,20,21,24],free_mem:1,freesurf:[1,4,12,19,20,21],freesurfer_hom:24,from:[1,2,3,8,16,19,20,21,23,24],from_dict:1,from_fil:[3,4,5],front:19,fs_licens:24,fs_license_fil:1,fs_subjects_dir:1,fsl:[16,21],full:[1,10,12,19,23],full_spher:5,fullds005:24,fund:24,further:[23,24],futur:[20,23,24],g742a18f:[1,24],garikoitz:19,gener:[1,4,16,20,21,24],generate_rasb:10,generate_vecv:10,get:[1,10,21,23,24],get_linked_lib:1,get_plugin:1,gibb:23,gihub:19,git:20,github:[19,20,24],given:[1,10],googl:[1,20],gradient:[5,10,14,23],gradients_rasb:14,graph:[1,12,14,16,24],grid:24,guid:23,guidelin:[19,20],habitu:21,had:16,half:10,halford:19,hand:21,handl:[5,7,8,20,21],happen:1,happi:20,hard:1,harvard:24,has:[1,9,20,21],has_fieldmap:14,hash:1,have:[10,21,23,24],head:[20,23],header:[1,2,24],health:19,hello:21,help:[20,24],hemispher:10,heurist:1,high:20,highli:24,hire:[1,24],histogram:16,hmc:23,hoc:20,holder:23,home:[1,24],hospit:19,host:[21,24],how:21,hpc:20,html:[1,4,10,16,24],http:[10,21,24],hub:21,idea:[20,21],identif:[19,23],identifi:[1,21,23,24],idiosyncrasi:20,ignor:[1,24],imag:[0,2,4,6,10,16,19,21,23,24],implement:[1,2,19,20,23],impli:24,improv:[19,21,24],imput:23,in_bval:[5,14],in_bvec:[5,14],in_fil:[2,3,8,16],in_rasb:5,includ:[19,20,23,24],inconsist:19,increas:24,index:[3,16],indic:[16,24],individu:16,infer:20,info:1,inform:[0,1,12,24],infrastructur:[19,21],inhomogen:23,init:[1,24],init_dmriprep_wf:12,init_dwi_preproc_wf:14,init_dwi_reference_wf:[14,16],init_enhance_and_skullstrip_dwi_wf:16,init_enhance_and_skullstrip_wf:16,init_reportlets_wf:[14,15],init_single_subject_wf:12,init_spac:1,initi:[1,16,19,24],input:[2,3,4,5,7,8,12,14,16,24],input_bids_path:21,instal:[1,20,24],instanc:[1,12,19],instead:19,institut:19,instruct:21,integ:[3,5],integr:[19,23],intend:24,intens:[8,16,23],interfac:[1,19,20,21],intermedi:[1,24],interpret:[20,21],intersect:16,intervent:20,introduc:20,inu:[16,23],inventori:20,iowa:19,issu:[1,19,20],item:[2,3,4,5],iter:[1,16,19],its:16,jame:19,januari:20,join:1,joseph:19,json:[1,24],just:10,keep:[1,24],kei:[2,24],kent:19,kernel:[1,21],keshavan:19,keyword:24,known:21,kwarg:2,label:[12,14,24],laptop:20,larg:[19,20],last:[8,10],latest:[16,24],latex:[1,24],lausann:19,layout:[1,24],lead:23,learn:20,least:24,left:[1,2],leftov:19,length:10,lerma:19,less:1,level:[1,21,24],leverag:23,librari:[1,20],licens:[1,19,20,21],lie:10,lightweight:21,like:[1,20,23],limit:[1,20,21,24],line:[1,20,21],linear:23,lineno:1,link:[1,19],lint:19,linux:[1,21],list:[1,2,3,4,5,10,12,16,20,21,24],load:[1,19],loadtxt:5,local:[19,24],locat:[10,15,24],log:[0,20,24],log_dir:1,log_level:1,logger:1,logitudin:1,longitudin:[1,24],look:[1,20],loos:16,low:[10,24],low_mem:1,machin:21,magic:1,mai:[12,16,19,20,24],maint:19,maintain:[1,20],mainten:19,major:23,make:[9,10,20,21,23],makefil:19,manag:1,mandatori:[2,3,5],mani:21,manual:[20,24],manuscript:19,map:20,march:20,mark:19,markdown:1,mask:[3,10,14,16,24],mask_fil:[3,8,10,16],master:24,mathemat:16,mattermost:20,matthew:19,maximum:[16,24],maxtasksperchild:1,md_only_boilerpl:1,mean:[1,10,24],measur:23,median:[8,16,24],medicin:19,mem:24,mem_gb:16,mem_mb:24,memori:[1,24],memory_gb:[1,24],mental:19,merg:23,messag:[1,21],meta_dict:2,metadata:2,metal:21,method:[0,21,24],methodolog:16,mgh:24,mgr:1,michael:19,migrat:19,mileston:[19,20],millimet:24,minim:[1,19],minor:19,misc:[0,6],miscellan:9,modal:14,mode:[1,19],model:[20,23],modifi:[21,24],modul:[0,1,2,6,11,13,17,19],monitor:[1,24],more:[19,20,21],morpholog:16,most:[10,19,21],motion:[20,23],move:19,mri:[12,14,20],multi:21,multiproc:1,multiprocess:1,multithread:1,must:[1,10,21,24],mutual:5,n4biasfieldcorrect:16,n_cpu:24,name:[2,15,16,19,20,21],named_opt:21,ndarrai:10,necessari:21,need:[1,12],neurodock:21,neurohackademi:19,neuroimag:[20,21],neurosci:19,neuroscientist:20,neurostar:20,newer:20,newrasb:5,next:21,nice:20,nifti:[1,2,14,16],nii:[3,5],niprep:[19,20,21,24],nipyp:[1,2,3,4,5,19,20,21,24],nipype_vers:1,niworkflow:[2,7,16,19],nmr:24,node:[1,16,24],non:[1,4,10,23,24],none:[1,2,3,4,5,8,10],nonstandard:1,norm:10,norm_val:10,norm_vec:10,normal:[10,14,24],normalize_gradi:10,note:24,notrack:[1,24],notrecommend:24,novemb:20,now:24,nproc:[1,24],nstd_space:4,nthread:24,number:[1,10,12,16,24],numer:20,numpi:[2,10],oasis30:1,object:[1,2,3,4,5,10],obtain:[21,24],occurr:24,octob:20,oesteban:1,oldrasb:5,omp:24,omp_nthread:[1,16,24],on_fail:19,onc:21,one:[12,14,16,24],ones:10,onli:[1,24],onlin:24,oper:[1,10,21,24],oppos:12,opt:[1,24],option:[1,2,4,5,19,20,21],orchestr:14,org:[20,24],organ:12,orient:[10,24],origin:24,oscar:19,osf:19,other:[0,16,19,20,21,23],otherwis:1,othewis:10,our:[19,20,21],out:[1,19,21,24],out_b0:3,out_bval:5,out_bvec:5,out_dict:2,out_fil:[2,3],out_meta:2,out_path:8,out_path_bas:2,out_rasb:5,out_ref:3,out_report:[4,16],outcom:24,outlier:23,output:[0,1,2,3,4,5,11,13,14,16,19,20,21,24],output_dir:[1,15,24],output_spac:[1,24],over:[1,3],overal:20,overcommit:1,overcommit_limit:1,overcommit_polici:1,overdu:19,overhaul:19,packag:[0,19,20,21],page:19,pair:10,pandoc:24,parallel:[1,16],paramet:[1,10,12,14,16,24],parameter:1,parameterize_dir:1,part:24,particip:[1,24],participant_id:1,participant_label:[1,7,24],particular:[1,20],pass:[1,24],patch:2,path:[1,2,10,14,19,21,24],pathlik:[2,3,4,5,12,14],pca:23,pdf:[12,14,16],pennsylvania:19,per:24,perelman:19,perform:[12,16,20],philosophi:20,pickl:1,pin:19,pip:21,pipelin:[12,20,23],pisner:19,plan:[1,20],platform:1,pleas:[19,20,21,24],plugin:[1,19,24],plugin_arg:1,png:[12,14,16],point:[10,23,24],poldrack:19,pole:[5,10],polici:1,pop:20,popul:12,popular:21,popylar:[19,24],port:[19,23],posit:20,posix:1,posixpath:1,possibl:[1,23,24],pre_mask:16,preambl:21,prefix:[9,24],prep:19,prepar:[12,19,20,24],preprocess:[1,12,14,20],present:9,previou:[19,24],price:21,princip:24,principl:19,pro:20,probabl:21,process:[1,12,14,16,19,20,23,24],produc:21,program:[19,20,24],project:[1,20],propag:2,properti:10,provid:[20,24],psycholog:19,pub:10,pull:21,pybid:24,pypi:21,python:[1,20],qsiprep:23,qualiti:[20,24],queri:20,question:20,radiolog:19,rais:19,raise_error:10,raise_inconsist:10,raise_insuffici:1,ram:1,random:24,rapid:20,rasb:[10,14],rasb_dwi_length_check:10,rasb_fil:10,raw:[10,23],raw_ref_imag:16,read:[1,21],readi:21,readm:19,real:24,realli:10,reason:[21,24],recent:10,recommend:[20,24],recon:[1,12,24],reconal:24,reconstruct:[1,24],record:24,redirect:1,redirect_warn:1,reduc:24,ref_imag:16,ref_image_brain:16,refactor:19,refer:[1,10,14,16,19,24],regard:1,regardless:12,regist:[1,14,16,24],registr:[19,20,23],registri:19,regular:1,rel:[10,21],relat:20,releas:[19,23],remov:[1,16,19,24],reorgan:19,reorient:[10,19],reorient_rasb:10,replac:[1,7],replic:24,report:[0,1,2,12,15,19,24],reportlet:[1,4,15,16,24],reportlets_wf:15,reports_bug:19,reports_onli:1,repres:[1,2,3,4,5],represent:[1,19],reproduc:20,requir:[21,24],rerun:24,res:[3,24],resampl:24,rescal:[3,8,16,23],rescale_b0:[3,8],rescaleb0:3,research:20,resolut:24,resourc:[1,24],resource_monitor:[1,3,4,5],respons:[0,20],result:[1,10,20,23,24],resultinb:10,retval:1,reus:24,revis:19,richi:19,rician:23,right:15,ring:23,road:20,roadmap:[19,20],robust:20,roi:2,rokem:19,roll:19,root:[1,24],rootlogg:1,rstudio:10,rtol:5,run:[1,3,5,12,14,16,19,21,23,24],run_reconal:1,run_unique_id:1,run_uuid:[1,24],runtim:[1,24],russel:19,salient:19,same:21,sampl:24,save:[2,19],sbref:[2,24],scale:14,scan:19,school:19,score:10,scott:20,script:19,sdc:24,sdc_report:15,sdcflow:23,search:24,section:[0,20,21],secur:21,see:[1,20,21,24],seed:[1,24],segment:4,select:[1,24],send:24,sent:21,sentri:19,separ:[12,24],septemb:20,seri:[3,10,24],serv:[19,23],session:[1,12,19],set:[1,12,15,19,20,21,24],sever:[12,23],sfm:23,sha256:1,shape:10,share:[1,21],sharpen:16,shell:[10,23],shorelin:23,should:[1,2,21,23,24],show:[19,21,24],signal:[3,8,10,16,23],signal_drift:3,simpleinterfac:[2,3,4,5],simpli:24,singl:[1,12,16,23,24],singleton:1,singular:[20,24],skip:24,skiprow:5,skull:[1,16,24],skull_strip_fixed_se:1,skull_strip_templ:[1,24],skull_stripped_fil:16,skullstrip:19,sloppi:[1,19,24],small:19,smoke:19,smriprep:[1,19],snowbal:20,softwar:[20,21,23,24],some:[1,19,20,21,24],someth:21,somewher:20,sourc:[2,12,14,16],source_fil:2,space:[1,4,20,24],spatial:[1,24],spatialrefer:1,specif:[0,19,20],specifi:[21,24],speed:24,spend:23,sphere:[10,16],spline:[1,24],sprint:19,squar:[10,24],stage:24,stake:23,standard:[1,4,10,16,20,24],stanford:19,start:[1,19,20,21],state:20,statist:24,std_space:4,step:[1,16,19,20,21,23],still:20,stop:[1,24],stop_on_first_crash:1,store:[1,2,15,24],str:[1,2,3,5,10,12,16],stream:21,string:[1,2,3,4,5],strip:[1,16,24],structur:[1,2,4,10,16,21,24],sty:19,sub:[1,9,12,19,24],sub_prefix:9,subid:9,subject:[1,4,9,12,24],subject_data:2,subject_id:[2,4,12],subjects_dir:[4,12],subjectsummari:4,submit:[19,20],submm:24,submodul:[0,20],suboptim:1,subpackag:[0,20],subprocess:1,successfulli:24,suffix:24,summari:4,summaryinterfac:4,support:[19,20],sure:[9,20,21],surfac:[1,20],surfer:24,suscept:[1,14,20,23],svg:[12,14,16,19],syn:20,system:[9,21,24],t1w:[2,4,19,23,24],t2w:[2,4],tabl:[5,10,14],tacc:21,tag:19,take:[16,20,24],target:[1,19,20],task:[1,19],task_id:19,technolog:20,templat:[1,12,24],templateflow:1,templateflow_hom:1,templateflow_vers:1,temporari:24,tenant:21,term:20,termin:21,test:[19,23,24],texa:19,text:1,thei:23,them:[16,19,23],therefor:21,thesee:23,thi:[1,9,10,12,16,19,20,21,23,24],thp0005:1,thp002:1,thread:[16,24],threshold:10,through:24,time:[1,3,23,24],tip:21,tmp:1,tmpdir:[3,5],to_filenam:[1,10],tolist:10,tomatch:2,toml:1,took:21,tool:[1,3,19,20,21,24],top:24,traceback:10,track:[1,19,20],transform:10,transpar:20,travisci:19,treat:24,trick:[1,21],tsv:5,tupl:5,two:[12,21],txt:[1,24],type:10,typo:19,ubuntu:21,uncompress:[1,2],under:[1,21],uniform:23,uniqu:1,unit:[10,19],univers:19,unless:24,unmodifi:2,updat:[19,20],upon:20,upper:24,upstream:19,usa:19,usabiaga:19,usag:[0,19,20,21],use:[1,16,19,20,21,23,24],use_plugin:24,use_syn:1,used:[1,14,21,23,24],useful:1,user:[1,21,23],uses:24,using:[1,8,12,16,19,21,23,24],usr:1,util:[0,1,11,13,19,20],uuid:24,val:19,valid:[16,20,21,23,24],validate_input_dir:7,validation_report:16,valu:[1,2,5,10,14,16,24],valueerror:10,variabl:[1,24],variat:10,varieti:20,variou:23,vec:[10,19],vector:[0,2,6,14,19],veraart:19,verbos:[1,24],veri:24,version:[1,4,7,16,19,20,21,24],via:1,video:[19,20],virtual:[1,20,21],visit:21,visual:24,volum:[3,8,10,16,23,24],vstack:10,vvv:24,wai:[10,21,23],want:[20,24],warn:1,washington:19,websit:19,weight:10,welcom:20,well:23,were:21,what:20,when:[1,19,24],whenev:1,where:[1,10,20,23,24],whether:[1,2,10,16,24],which:[1,2,3,4,5,10,19,20,21,24],whole:20,wide:1,within:[10,21,24],without:[20,24],work:[1,19,21,24],work_dir:[1,24],workdir:24,workflow:[0,1,9,19,20,21],world:[21,24],would:23,write:[1,10,15,19,24],write_derivative_descript:7,write_graph:1,written:[1,21],www:24,xxxxx:24,year:19,you:[20,21,24],your:[20,21,24],yourself:20,z_thre:10,zenodo:19,zero:10},titles:["Library API (application program interface)","dmriprep.config package","dmriprep.interfaces package","dmriprep.interfaces.images module","dmriprep.interfaces.reports module","dmriprep.interfaces.vectors module","dmriprep.utils package","dmriprep.utils.bids module","dmriprep.utils.images module","dmriprep.utils.misc module","dmriprep.utils.vectors module","dmriprep.workflows package","dmriprep.workflows.base module","dmriprep.workflows.dwi package","dmriprep.workflows.dwi.base module","dmriprep.workflows.dwi.outputs module","dmriprep.workflows.dwi.util module","dmriprep.workflows.fmap package","dmriprep.workflows.fmap.base module","What\u2019s new?","dMRIPrep","Installation","&lt;no title&gt;","Development road map","Usage"],titleterms:{"1a0":19,"1st":23,"long":23,"new":19,The:24,about:20,analyt:24,ant:24,api:0,applic:0,april:23,argument:24,author:19,base:[12,14,18,19],bid:[7,24],cloud:21,command:24,commerci:21,config:1,configur:[1,24],contain:21,content:20,correct:24,decemb:19,depend:21,develop:23,distort:24,dmriprep:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],docker:21,dwi:[13,14,15,16],environ:21,execut:24,extern:21,fieldmap:24,filter:24,fmap:[17,18],format:24,freesurf:24,get:20,googl:24,handl:24,hpc:21,imag:[3,8],instal:21,interfac:[0,2,3,4,5],involv:20,januari:19,laptop:21,librari:0,licens:24,line:24,list:19,log:1,mai:23,manual:21,map:23,march:23,misc:9,modul:[3,4,5,7,8,9,10,12,14,15,16,18],name:24,novemb:19,octob:19,option:24,other:[1,24],output:15,packag:[1,2,6,11,13,17],paper:19,perform:24,plan:23,posit:24,prepar:21,preprocess:24,program:0,python:21,queri:24,recommend:21,registr:24,report:4,respons:1,road:23,section:1,septemb:[19,23],seri:19,singular:21,specif:24,submodul:[2,6,11,13,17],subpackag:11,surfac:24,syn:24,target:23,technolog:21,term:23,track:24,usag:[1,24],util:[6,7,8,9,10,16],vector:[5,10],version:23,what:19,workflow:[11,12,13,14,15,16,17,18,24]}})