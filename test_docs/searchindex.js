Search.setIndex({docnames:["api","api/dmriprep.config","api/dmriprep.interfaces","api/dmriprep.interfaces.reports","api/dmriprep.interfaces.vectors","api/dmriprep.utils","api/dmriprep.utils.bids","api/dmriprep.utils.vectors","api/dmriprep.workflows","api/dmriprep.workflows.base","api/dmriprep.workflows.dwi","changes","index","installation","links","usage"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.index":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,sphinx:56},filenames:["api.rst","api/dmriprep.config.rst","api/dmriprep.interfaces.rst","api/dmriprep.interfaces.reports.rst","api/dmriprep.interfaces.vectors.rst","api/dmriprep.utils.rst","api/dmriprep.utils.bids.rst","api/dmriprep.utils.vectors.rst","api/dmriprep.workflows.rst","api/dmriprep.workflows.base.rst","api/dmriprep.workflows.dwi.rst","changes.rst","index.rst","installation.rst","links.rst","usage.rst"],objects:{"dmriprep.config":{dumps:[1,1,1,""],environment:[1,2,1,""],execution:[1,2,1,""],from_dict:[1,1,1,""],get:[1,1,1,""],init_spaces:[1,1,1,""],load:[1,1,1,""],loggers:[1,2,1,""],nipype:[1,2,1,""],redirect_warnings:[1,1,1,""],to_filename:[1,1,1,""],workflow:[1,2,1,""]},"dmriprep.config.environment":{cpu_count:[1,3,1,""],exec_docker_version:[1,3,1,""],exec_env:[1,3,1,""],free_mem:[1,3,1,""],nipype_version:[1,3,1,""],overcommit_limit:[1,3,1,""],overcommit_policy:[1,3,1,""],templateflow_version:[1,3,1,""],version:[1,3,1,""]},"dmriprep.config.execution":{bids_description_hash:[1,3,1,""],bids_dir:[1,3,1,""],bids_filters:[1,3,1,""],boilerplate_only:[1,3,1,""],debug:[1,3,1,""],fs_license_file:[1,3,1,""],fs_subjects_dir:[1,3,1,""],init:[1,4,1,""],layout:[1,3,1,""],log_dir:[1,3,1,""],log_level:[1,3,1,""],low_mem:[1,3,1,""],md_only_boilerplate:[1,3,1,""],notrack:[1,3,1,""],output_dir:[1,3,1,""],output_spaces:[1,3,1,""],participant_label:[1,3,1,""],reports_only:[1,3,1,""],run_uuid:[1,3,1,""],templateflow_home:[1,3,1,""],work_dir:[1,3,1,""],write_graph:[1,3,1,""]},"dmriprep.config.loggers":{"default":[1,3,1,""],"interface":[1,3,1,""],cli:[1,3,1,""],init:[1,4,1,""],utils:[1,3,1,""],workflow:[1,3,1,""]},"dmriprep.config.nipype":{crashfile_format:[1,3,1,""],get_linked_libs:[1,3,1,""],get_plugin:[1,4,1,""],init:[1,4,1,""],memory_gb:[1,3,1,""],nprocs:[1,3,1,""],omp_nthreads:[1,3,1,""],plugin:[1,3,1,""],plugin_args:[1,3,1,""],resource_monitor:[1,3,1,""],stop_on_first_crash:[1,3,1,""]},"dmriprep.config.workflow":{anat_only:[1,3,1,""],fmap_bspline:[1,3,1,""],fmap_demean:[1,3,1,""],force_syn:[1,3,1,""],hires:[1,3,1,""],ignore:[1,3,1,""],longitudinal:[1,3,1,""],run_reconall:[1,3,1,""],skull_strip_fixed_seed:[1,3,1,""],skull_strip_template:[1,3,1,""],spaces:[1,3,1,""],use_syn:[1,3,1,""]},"dmriprep.interfaces":{BIDSDataGrabber:[2,2,1,""],BIDSDataGrabberOutputSpec:[2,2,1,""],DerivativesDataSink:[2,2,1,""],reports:[3,0,0,"-"],vectors:[4,0,0,"-"]},"dmriprep.interfaces.BIDSDataGrabber":{input_spec:[2,3,1,""],output_spec:[2,3,1,""]},"dmriprep.interfaces.DerivativesDataSink":{out_path_base:[2,3,1,""]},"dmriprep.interfaces.reports":{AboutSummary:[3,2,1,""],AboutSummaryInputSpec:[3,2,1,""],SubjectSummary:[3,2,1,""],SubjectSummaryInputSpec:[3,2,1,""],SubjectSummaryOutputSpec:[3,2,1,""],SummaryInterface:[3,2,1,""],SummaryOutputSpec:[3,2,1,""]},"dmriprep.interfaces.reports.AboutSummary":{input_spec:[3,3,1,""]},"dmriprep.interfaces.reports.SubjectSummary":{input_spec:[3,3,1,""],output_spec:[3,3,1,""]},"dmriprep.interfaces.reports.SummaryInterface":{output_spec:[3,3,1,""]},"dmriprep.interfaces.vectors":{CheckGradientTable:[4,2,1,""]},"dmriprep.interfaces.vectors.CheckGradientTable":{input_spec:[4,3,1,""],output_spec:[4,3,1,""]},"dmriprep.utils":{bids:[6,0,0,"-"],vectors:[7,0,0,"-"]},"dmriprep.utils.bids":{collect_data:[6,1,1,""],validate_input_dir:[6,1,1,""],write_derivative_description:[6,1,1,""]},"dmriprep.utils.vectors":{DiffusionGradientTable:[7,2,1,""],bvecs2ras:[7,1,1,""],calculate_pole:[7,1,1,""],normalize_gradients:[7,1,1,""]},"dmriprep.utils.vectors.DiffusionGradientTable":{affine:[7,4,1,""],b0mask:[7,4,1,""],bvals:[7,4,1,""],bvecs:[7,4,1,""],generate_rasb:[7,4,1,""],generate_vecval:[7,4,1,""],gradients:[7,4,1,""],normalize:[7,4,1,""],normalized:[7,4,1,""],pole:[7,4,1,""],reorient_rasb:[7,4,1,""],to_filename:[7,4,1,""]},"dmriprep.workflows":{base:[9,0,0,"-"],dwi:[10,0,0,"-"]},"dmriprep.workflows.base":{init_dmriprep_wf:[9,1,1,""],init_single_subject_wf:[9,1,1,""]},"dmriprep.workflows.dwi":{init_dwi_preproc_wf:[10,1,1,""],init_dwi_reference_wf:[10,1,1,""]},dmriprep:{config:[1,0,0,"-"],interfaces:[2,0,0,"-"],utils:[5,0,0,"-"],workflows:[8,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","attribute","Python attribute"],"4":["py","method","Python method"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:attribute","4":"py:method"},terms:{"184610_855f740d":1,"1a0":12,"27121_a22e51b47c544980bad594d5e0bb2d04":7,"4b66":1,"54a8":1,"885a":1,"class":[0,1,2,3,4,7],"default":[1,10,15],"export":1,"float":7,"function":[0,1,13],"import":1,"int":[7,10],"new":[1,12,13],"return":7,"static":7,"switch":1,"true":[1,4,6,7],"try":13,ARS:7,For:[13,15],LAS:7,LPS:7,RAS:7,The:[1,7,12,13],Then:10,There:13,These:13,_bidsdatagrabberinputspec:2,_bidsdatagrabberoutputspec:2,_checkgradienttableinputspec:4,_checkgradienttableoutputspec:4,_config:1,about:9,aboutsummari:3,aboutsummaryinputspec:3,abov:13,absenc:1,access:1,acquisit:12,across:1,action:1,adapt:[10,12],add:1,addit:13,address:12,adher:[11,13],advanc:12,affin:[7,10],afni:[12,13],after:[1,13],agnost:12,ahead:13,algorithm:12,alia:[2,3,4],all:[1,7,9,13],allclos:4,alloc:1,allow:[1,13],allowed_ent:2,also:[11,13],altern:[1,13],amazonaw:7,ambiti:13,amd64:13,amplitud:7,analysi:12,analysis_level:13,analyt:1,anat_onli:1,anatom:[1,9,11],ani:[1,9,12],ant:[12,13],api:12,app:[13,15],appear:13,applic:12,approach:13,arg:[1,2],argument:[1,12,13],arrai:7,attempt:11,autom:[1,13],automat:12,avail:[1,12,13],b0_ix:10,b0_threshold:7,b0mask:7,b0s:10,b7671905ccb2:1,b_scale:7,back:11,bare:13,base:[0,1,2,3,4,7,8,12,13],baseinterfaceinputspec:3,bash:13,basi:1,basic:12,becom:12,been:7,befor:12,below:7,best:12,better:12,bid:[0,1,2,5,12,13],bids_description_hash:1,bids_dir:[1,6],bids_filt:1,bids_root:15,bids_valid:6,bidsdatagrabb:2,bidsdatagrabberoutputspec:2,bidslayout:1,big:11,binari:13,boilerpl:1,boilerplate_onli:1,brain:[1,12],branch:11,breed:12,bring:11,build:[1,10,12,13],build_workflow:1,built:1,bval:[4,7],bval_fil:10,bvec:[4,7],bvec_fil:10,bvec_norm_epsilon:7,bvecs2ra:7,c3d:13,cach:1,calcul:[7,10],calculate_pol:7,call:[1,7],can:[1,12,13],capabl:[11,13],categori:1,challeng:12,chang:1,chdir:4,check:[4,7,13],checkgradientt:4,checkout:13,checkpoint:1,checksum:1,chose:13,classmethod:1,clean:12,cleanenv:15,cli:1,client:[1,13],cloud:12,code:[1,9,10],collect:[1,9],collect_data:6,com:[7,13],come:13,command:[1,12,13],commerci:12,common:15,compar:13,complex:12,compliant:1,compos:[7,13],comprehend:9,comput:1,config:[0,12],config_fil:1,configur:[0,12,13],consid:7,consist:1,consumpt:1,contact:13,contain:[1,12,15],container_command_and_opt:13,container_imag:13,content:11,continu:[1,11],contrast:10,control:10,conveni:1,convers:[1,7],convert:[1,7],coordin:7,copi:1,core:[2,3,4],coregistr:12,correct:4,correctli:13,correspond:[1,7],cover:7,cpu:1,cpu_count:1,crashfil:1,crashfile_format:1,crawl:1,creat:[1,9,12,13],current:[1,13],custom:[2,10],daemon:13,data:[7,12,15],data_dir:4,dataset:[1,10,12,15],dataset_descript:1,datasink:2,debian:13,debug:1,definit:15,depend:[12,15],deploi:13,deploy:11,deriv:[1,9],deriv_dir:6,derivatives_path:13,derivativesdatasink:2,descript:[1,13],design:[1,12],dict:1,dictionari:1,diffus:[7,9,10,12],diffusiongradientt:7,direct:9,directori:1,disabl:15,disk:1,distort:1,dmri:[10,12],dmriprep:[0,11,13,15],dmriprep_named_opt:13,doc:13,docker:[1,12,15],dockerfil:13,dockerout:15,document:[12,13],doe:1,drop:13,dump:1,dwi:[0,4,7,8,9,15],dwi_fil:[4,7,10],dwi_mask:10,dwi_reference_wf:10,each:[1,9,10,12],earli:1,easi:12,easili:[1,12],edu:15,either:1,enabl:1,encompas:12,engin:[1,13],enhanc:10,enlist:1,ensur:[4,12],entiti:9,environ:[1,12,15],equip:12,error:1,estim:1,etc:[1,12],everi:1,exact:15,exampl:[4,7,13,15],exec_docker_vers:1,exec_env:[1,6],execut:[1,9,12,13],exercis:11,exist:1,extern:12,extra:13,extract:[1,10],eye:7,fals:[1,7],field:1,fieldmap:[1,15],file:[1,7,10,13,15],filenam:[1,7],filesystem:1,filetyp:7,filter:1,first:[1,11,13,15],fit:12,fix:1,flag:[1,15],flat:1,fmap_bsplin:1,fmap_demean:1,fmriprep:11,folder:[1,9],follow:[13,15],force_syn:1,forkserv:1,format:[1,12],found:[1,13],frame:7,framework:13,free:[1,13,15],free_mem:1,freesurf:[1,9,12,13],freesurfer_hom:15,from:[1,10,12,13],from_dict:1,from_fil:[3,4],fs_licens:15,fs_license_fil:1,fs_subjects_dir:1,fsl:[12,13],full:[7,9],full_spher:4,fullds005:15,g3aec266:1,gener:[1,3,10,12,13],generate_rasb:7,generate_vecv:7,get:[1,7,13],get_linked_lib:1,get_plugin:1,github:11,given:[1,7],googl:1,gradient:[4,7],graph:[1,9,10],habitu:13,had:10,half:7,hand:13,handl:[4,6,13],happen:1,hard:1,harvard:15,has:[1,12,13],have:[7,13],hello:13,help:12,hemispher:7,heurist:1,high:12,highli:15,hire:1,hoc:12,home:15,host:[13,15],how:13,hpc:12,html:[1,7,10,15],http:[7,13,15],hub:13,idea:13,identifi:[1,13],idiosyncrasi:12,ignor:[1,15],imag:[7,10,13,15],implement:[1,12],improv:13,in_bval:4,in_bvec:4,in_rasb:4,includ:[12,15],index:10,indic:10,individu:10,infer:12,info:1,inform:[0,1,9],infrastructur:13,init:1,init_dmriprep_wf:9,init_dwi_preproc_wf:10,init_dwi_reference_wf:10,init_enhance_and_skullstrip_wf:10,init_reportlets_wf:10,init_single_subject_wf:9,init_spac:1,initi:1,input:[2,3,4,6,9,10,15],input_bids_path:13,input_spec:[2,3,4],instal:[1,12,15],instanc:[1,9],instruct:13,integr:11,intens:10,interfac:[1,12,13],intermedi:1,interpret:[12,13],intervent:12,inventori:12,involv:12,issu:1,its:10,join:1,json:1,just:7,keep:1,kei:15,kernel:[1,13],known:[12,13],kwarg:[2,3],label:9,laptop:12,larg:12,last:7,latest:15,latex:1,layout:1,least:15,left:1,length:7,less:1,level:[1,13],librari:[1,12],licens:[1,12,13],lie:7,lightweight:13,like:1,limit:[1,13],line:[1,12,13],lineno:1,link:1,linux:[1,13],list:[1,7,9,10,13],load:1,loadtxt:4,local:15,locat:[7,15],log:[0,12],log_dir:1,log_level:1,logger:1,logitudin:1,longitudin:1,look:1,low:7,low_mem:1,machin:13,magic:1,mai:[9,10],maintain:1,make:[7,13],manag:1,mani:13,manual:[12,15],mark:11,markdown:1,mask:[7,10],maximum:10,maxtasksperchild:1,md_only_boilerpl:1,mean:1,median:10,memori:1,memory_gb:1,messag:[1,13],metal:13,method:[0,13,15],methodolog:10,mgh:15,mgr:1,minim:1,mode:1,model:12,modifi:13,modul:[0,1,2,5,8],monitor:1,more:13,most:[7,13],mri:[9,12],multi:13,multiproc:1,multiprocess:1,multithread:1,must:[1,7,13,15],name:[10,13],named_opt:13,ndarrai:7,necessari:13,need:[1,9],neurodock:13,neuroimag:[12,13],neuroscientist:12,neurostar:12,newer:12,newrasb:4,next:13,nifti:[1,10],nii:4,nilearn:12,niprep:[13,15],nipyp:[1,2,3,4,12,13],nipype_vers:1,niworkflow:[2,6,10],nmr:15,non:[1,7],none:[1,2,3,4,7],nonstandard:1,norm:7,norm_val:7,norm_vec:7,normal:[7,12],normalize_gradi:7,notrack:1,novemb:12,nproc:1,number:[1,7,9,10],numer:12,numpi:7,oasis30:1,object:[1,7],obtain:[13,15],oldrasb:4,omp_nthread:[1,10],onc:13,one:[9,15],ones:7,onli:1,onlin:15,oper:[1,7,13],oppos:9,opt:[1,15],option:[1,13],org:12,organ:9,other:[0,10,12,13],othewis:7,our:13,out:[1,11,13,15],out_path_bas:2,out_rasb:4,output:[1,4,10,12,13],output_dir:1,output_spac:1,output_spec:[2,3,4],overcommit:1,overcommit_limit:1,overcommit_polici:1,packag:[0,12,13],pair:7,parallel:1,paramet:[1,7,9,10],part:15,particip:[1,15],participant_id:1,participant_label:[1,6],particular:[1,12],pass:[1,15],patch:2,path:[1,7,10,13,15],pathlik:9,pdf:[9,10],perform:[9,12],pickl:1,pip:13,pipelin:[9,12],plan:1,platform:1,pleas:13,plugin:[1,11],plugin_arg:1,png:[9,10],point:[7,15],pole:[4,7],polici:1,popul:9,popular:13,posix:1,posixpath:1,possibl:[1,15],pre:10,preambl:13,prepar:[9,12,15],preprocess:[1,9,10,12],price:13,princip:15,principl:11,probabl:13,process:[1,9,10,11,12,15],produc:13,program:12,project:1,properti:7,provid:12,pub:7,pull:13,pypi:13,python:[1,12],qualiti:12,raise_insuffici:1,ram:1,rapid:12,rasb:7,rasb_fil:7,raw:7,raw_ref_imag:10,read:[1,13],readi:13,reason:13,recent:7,recommend:[12,15],recon:[1,9],reconstruct:1,redirect:1,redirect_warn:1,ref_imag:10,ref_image_brain:10,refactor:11,refer:[1,7,10],regard:1,regardless:9,regist:[10,15],registr:15,regular:1,rel:13,releas:11,remov:1,reorient:7,reorient_rasb:7,replac:6,report:[0,1,2,9],reportlet:[1,3,10],reports_onli:1,repres:1,reproduc:12,requir:[13,15],rescal:10,research:12,resourc:1,resource_monitor:[1,3,4],respons:[0,12],result:[1,7,12],resultinb:7,retval:1,robust:12,roll:11,root:1,rootlogg:1,rstudio:7,rtol:4,run:[1,4,9,11,13,15],run_reconal:1,run_unique_id:1,run_uuid:1,runtim:1,same:13,search:15,section:[0,12,13],secur:13,see:[1,13],seed:1,segment:12,select:1,sent:13,separ:9,septemb:12,seri:15,serv:11,session:9,set:[1,9,11,12,13,15],sever:9,sha256:1,shape:7,share:13,shell:7,should:[1,13],show:13,signal:10,simpleinterfac:[2,3,4],simpli:15,singl:[1,9],singleton:1,singular:[12,15],skiprow:4,skull:[1,10],skull_strip_fixed_se:1,skull_strip_templ:1,skullstrip:12,sloppi:1,smriprep:11,snowbal:12,softwar:[12,13],some:[1,13],someth:13,sourc:[9,10],space:1,spatial:1,spatialrefer:1,spec:3,specif:0,specifi:13,sphere:7,spline:1,squar:7,stage:10,standard:[1,12],start:[1,11,13],state:12,step:[1,12,13],stop:1,stop_on_first_crash:1,store:[1,15],str:[1,4,9,10],stream:13,string:1,strip:[1,10],structur:[1,7,13,15],sub:[1,9],subject:[1,9],subject_id:9,subjects_dir:9,subjectsummari:3,subjectsummaryinputspec:3,subjectsummaryoutputspec:3,submit:12,submodul:[0,12],suboptim:1,subpackag:[0,12],subprocess:1,summaryinterfac:3,summaryoutputspec:3,support:12,sure:13,surfac:1,surfer:15,suscept:1,svg:[9,10],system:[13,15],t1w:15,tabl:[4,7],tacc:13,tag:11,take:[10,15],target:1,task:1,technolog:12,templat:[1,9],templateflow:1,templateflow_hom:1,templateflow_vers:1,tenant:13,termin:13,test:11,text:1,them:10,therefor:13,thi:[1,9,10,11,12,13],thread:10,threshold:7,time:1,tip:13,tmpdir:4,to_filenam:[1,7],tolist:7,toml:1,took:13,tool:[1,12,13,15],traceback:7,track:1,tractographi:12,traitedspec:3,transform:7,transpar:12,trick:[1,13],tsv:4,two:[9,13],txt:[1,15],type:7,ubuntu:13,uncompress:1,under:[1,13],uniqu:1,unit:7,unless:15,unwarp:12,updat:12,upon:12,usag:[0,12,13],use:[10,12,13,15],use_syn:1,used:[1,13],useful:1,user:[1,13],uses:15,using:[1,9,10,13,15],util:[0,1,12],valid:[10,12,13,15],validate_input_dir:6,validation_report:10,valu:[1,7,10],valueerror:7,variabl:[1,15],varieti:12,vec:7,vector:[0,2,5,10],verbos:1,version:[1,6,10,13],via:1,virtual:[1,12,13],visit:13,volum:7,vstack:7,wai:13,warn:1,well:12,were:13,what:12,when:[1,15],whenev:1,where:[1,7,15],whether:[1,7,10],which:[1,7,12,13,15],whole:12,wide:1,within:13,without:12,work:[1,13,15],work_dir:1,workflow:[0,1,12,13,15],world:13,write:[1,7],write_derivative_descript:6,write_graph:1,written:[1,13],you:[13,15],your:[13,15],zenodo:11,zero:7},titles:["Library API (application program interface)","dmriprep.config package","dmriprep.interfaces package","dmriprep.interfaces.reports module","dmriprep.interfaces.vectors module","dmriprep.utils package","dmriprep.utils.bids module","dmriprep.utils.vectors module","dmriprep.workflows package","dmriprep.workflows.base module","dmriprep.workflows.dwi package","What\u2019s new?","dMRIPrep","Installation","&lt;no title&gt;","Usage"],titleterms:{"1a0":11,"new":11,The:15,api:0,applic:0,argument:15,base:9,bid:[6,15],cloud:13,command:15,commerci:13,config:1,configur:1,contain:13,content:12,depend:13,dmriprep:[1,2,3,4,5,6,7,8,9,10,12],docker:13,dwi:10,environ:13,execut:15,extern:13,format:15,freesurf:15,hpc:13,instal:13,interfac:[0,2,3,4],laptop:13,librari:0,licens:15,line:15,log:1,manual:13,modul:[3,4,6,7,9],novemb:11,other:1,packag:[1,2,5,8,10],prepar:13,program:0,python:13,recommend:13,report:3,respons:1,section:1,septemb:11,singular:13,submodul:[2,5,8],subpackag:8,technolog:13,usag:[1,15],util:[5,6,7],vector:[4,7],what:11,workflow:[8,9,10]}})