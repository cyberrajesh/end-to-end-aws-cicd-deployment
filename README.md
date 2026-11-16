# end-to-end-aws-cicd-deployment
End-to-End AWS CI/CD using Jenkins, Docker, ECR and EC2
Automatic CI/CD deployment test.
[README.md](https://github.com/user-attachments/files/34899627/README.md)
# End-to-End AWS CI/CD Deployment

Automated CI/CD pipeline that builds, containerises and deploys a Python application to AWS using **Jenkins, Docker, Amazon ECR and Amazon EC2**.

## Architecture

```
Developer -> GitHub -> Jenkins -> Docker build -> Amazon ECR -> Amazon EC2 (running container)
```

## Tech Stack

| Area | Tools |
| --- | --- |
| Source control | Git, GitHub |
| CI/CD | Jenkins (Jenkinsfile pipeline) |
| Containers | Docker |
| Image registry | Amazon ECR |
| Hosting | Amazon EC2 |
| Application | Python (`app.py`), tests in `tests/` |

## Repository Structure

| File / Folder | Purpose |
| --- | --- |
| `app.py` | Python application |
| `requirements.txt` | Python dependencies |
| `tests/` | Automated tests |
| `Dockerfile` | Builds the application image |
| `.dockerignore` | Files excluded from the image |
| `Jenkinsfile` | Pipeline definition |

## Pipeline Stages

> Check this list against your Jenkinsfile and edit it so it matches exactly.

1. Checkout code from GitHub
2. Install dependencies and run tests
3. Build the Docker image
4. Push the image to Amazon ECR
5. Deploy the container to the EC2 instance

## How to Run

1. Launch an EC2 instance and install Docker.
2. Create an Amazon ECR repository.
3. Install Jenkins and add your AWS credentials in Jenkins.
4. Create a Jenkins pipeline job that points to this repository.
5. Push a code change to GitHub and watch the pipeline run.

## Result

- Every code change triggers an automatic build and deployment.
- Add a screenshot of a successful Jenkins build here.
- Add a screenshot of the running application here.

## What I Learned

- Writing a Jenkinsfile and automating a build and deploy flow
- Building Docker images and storing them in Amazon ECR
- Deploying containers on Amazon EC2

## Author

**Rajesh S** | rajeshdece2001@gmail.com
