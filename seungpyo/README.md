#Submission by SeungPyo Hong

Since there are too much files in the darkflow git (and GitHub doesn't accept uploading more than 100 files),
I'll just upload files that I've made by myself and added in the directory.

> YOU MUST DOWNLOAD THE CORRESPONDING DATASET FROM
> [http://cvlab.hanyang.ac.kr/tracker_benchmark/datasets.html]


###1. cvlab_script.bash
This file contains the parameters required when executing the ___flow___ program.
Please put this file at the same location with the ___flow___.

###2. my_convert.py
This python script will convert the *.txt(actually it's csv though) formatted ground truth files provided from HYU cvlab into VOC style XML files.
Please put this file at the same location with the ground truth file of each dataset.
__Example__
```
darkflow(root directory) /
|_Car1 (dataset directory) /
  |_ ann/, img/, ground_truth_rect.txt, ...
  |_ __my_convert.py__
|_Dog (dataset directory) /
  |_ ann/, img/, ground_truth_rect.txt, ...
  |_ __my_convert.py__
```
For more details, please read the report.
