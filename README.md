# ChurnWorkshop
Amazon SageMaker Customer Churn Prediction with XGBoost Workshop

# Workshop Instructions
_Note:  This workshop will create an ephemeral AWS acccount for each attendee.  This ephemeral account is not accessible after the workshop.  You can, of course, clone this GitHub repo and reproduce the entire workshop in your own AWS Account._

## 0. Logout of All AWS Consoles Across All Browser Tabs
If you do not logout of existing AWS Consoles, things will not work properly.

![AWS Account Logout](img/aws-logout.png)

_Please logout of all AWS Console sessions in all browser tabs._

## 1. Login to the Workshop Portal (aka Event Engine). 
Open https://dashboard.eventengine.run/

Using the hash code you got from workshop admins, paste the event-hash-login that will be shared with you in the browser window. 

Choose the Accept Terms & Login. 

![Event Engine Terms and Conditions](img/event-engine-terms.png)

Choose OTP.

![Choose OTP](img/choose_top.png)

Write the Email that the passcode will be sent to, and choose Send passcode.

![write your email](img/one_time_email_passcode.png)

Copy the One-time email passcode from your inbox and paste it here.

![Paste One time code](img/paste_time_email_passcode.png)

Set your name clicking on Set Team Name, and then choose AWS Console.

![Event Engine Dashboard](img/event-engine-dashboard.png)

## 2. Login to the **AWS Console**

![Event Engine AWS Console](img/event-engine-aws-console.png)

Take the defaults and click on **Open AWS Console**. This will open AWS Console in a new browser tab.

If you see this message, you need to logout from any previously used AWS accounts.

![AWS Account Logout](img/aws-logout.png)

_Please logout of all AWS Console sessions in all browser tabs._

Double-check that your account name is similar to `TeamRole/MasterKey` as follows:

![IAM Role](img/teamrole-masterkey.png)

If not, please logout of your AWS Console in all browser tabs and re-run the steps above!

## 3. Launch a SageMaker Notebook Instance

Open the [AWS Management Console](https://console.aws.amazon.com/console/home)

**Note:** This workshop has been tested on the US East (N. Virginia) (us-east-1) region. Make sure that you see **N.Virginia** on the top right hand corner of your AWS Management Console. If you see a different region, click the dropdown menu and select US East (N. Virginia).

In the AWS Console search bar, type `SageMaker` and select `Amazon SageMaker` to open the service console.

![SageMaker Console](img/setup_aws_console.png). 

Select `Notebook instances`.

![SageMaker Console](img/aws-sagemaker-dashboard.png).

## 4. Start the Jupyter Notebook
You should see a ml.t2.large Notebook instance in status `InService`.

Select `Open Jupyter`. 

![Start Jupyter](img/start_jupyter.png)

## 5. Start the Workshop!
Click the `xgboost_customer_churn-student.ipynb` in your Jupyter notebook and start the workshop!

![Start Workshop](img/start_workshop.png)
