<p align="center">
  <img src="./assets/github-hero.svg" alt="Farah Ben Harb — Cloud and DevOps engineering" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/farah-ben-harb">GitHub</a> ·
  <a href="https://www.linkedin.com/in/farah-ben-harb-b26845313/">LinkedIn</a> ·
  <a href="https://farah-me.vercel.app/">Portfolio</a> ·
  <a href="mailto:benharbfarah85@gmail.com">Email</a>
</p>

# Farah Ben Harb

**Cloud & DevOps Engineering Student**<br>
Platform Engineering · SRE · DevSecOps · MLOps

I design cloud-native delivery systems that make software easier to ship, observe and operate. As a final-year computer engineering student, I work across Azure and OpenStack, Kubernetes and GitOps, security automation, and ML-serving pipelines.

My focus is the boundary between application code and a dependable runtime: repeatable infrastructure, traceable artifacts, useful telemetry and delivery workflows that are safe to change.

## What I build

- **Delivery platforms** that turn source code into tested, scanned and traceable artifacts.
- **Cloud-native runtimes** with Kubernetes automation, GitOps reconciliation, health signals and operational visibility.
- **Applied AI platforms** that connect model lifecycle, API serving, data infrastructure and observability.

## Professional experience

### Devoteam — Cloud & DevOps Intern · Jul–Aug 2026

Worked on cloud delivery and platform operations across Azure, K3s/Kubernetes, Helm, Argo CD and Dynatrace. My contributions included infrastructure automation with Terraform, GitHub Actions delivery workflows, DevSecOps controls and MCP-assisted operations with Claude Desktop.

### Earlier engineering experience

- **Ooredoo — Immersion Internship · 2024–2025:** built a Python/Java log-analysis parser, search interfaces and statistical dashboards for interpreting operational data.
- **Tunisie Télécom — Introductory Internship · 2022–2023:** developed foundations in networking, systems and telecom infrastructure operations.

## Selected engineering systems

### [FootballMatch AI Platform](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops)

**Problem → build → evidence.** Make CPU-first football-video analysis reproducible instead of leaving it as a standalone inference script. I built an asynchronous FastAPI service around OpenCV sampling, YOLO11n detection, ByteTrack tracking and exploratory K-Means clustering, then connected the service to MLflow tracking/registry workflows, Docker, GHCR, Helm, Prometheus and Grafana. The repository documents two runtime paths — a K3s/Argo CD GitOps path and a separate Azure Container Apps demo — with CI validating tests and security controls.

[Repository](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops) · [CI workflow](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops/blob/main/.github/workflows/ci.yml) · [latest observed successful run](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops/actions/runs/43030421510) · [Azure deployment notes](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops/blob/main/docs/deployment/azure-container-apps.md)

### [DevoRecruiter](https://github.com/farah-ben-harb/devorecruiter) · [GitOps repository](https://github.com/farah-ben-harb/devorecruiter-gitops)

**Problem → build → evidence.** Bring together a multi-service recruiting application and a delivery model that can evolve independently from application code. The application monorepo combines Angular, NestJS, FastAPI RAG, PostgreSQL/TypeORM and n8n integration; the separate GitOps repository holds charts, manifests and Argo CD configuration. The mainline repositories demonstrate the architecture and CI controls, while Terraform Azure, Dynatrace and MCP extensions remain associated with their work branches rather than being presented as a finished production deployment.

[Application](https://github.com/farah-ben-harb/devorecruiter) · [GitOps](https://github.com/farah-ben-harb/devorecruiter-gitops) · [application workflow](https://github.com/farah-ben-harb/devorecruiter/blob/main/.github/workflows/pipeline.yml)

### [DevSecOps Incident Platform](https://github.com/farah-ben-harb/devsecops-incident-platform)

**Problem → build → evidence.** Create an incident service with operational signals and a release path that treats security as part of delivery. I built a FastAPI/PostgreSQL API with health, readiness and Prometheus metrics, then configured Jenkins stages for tests, secret and dependency checks, filesystem/image scanning, immutable image tags and optional GitOps delivery. The accompanying [GitOps repository](https://github.com/farah-ben-harb/gitops-delivery-platform) contains Kustomize, Argo CD, persistence, ServiceMonitor and Grafana configuration.

[Repository](https://github.com/farah-ben-harb/devsecops-incident-platform) · [Jenkins pipeline](https://github.com/farah-ben-harb/devsecops-incident-platform/blob/main/Jenkinsfile) · [actions history](https://github.com/farah-ben-harb/devsecops-incident-platform/actions) · [GitOps delivery](https://github.com/farah-ben-harb/gitops-delivery-platform)

### OpenStack / Kubernetes automation

**Problem → build → evidence.** Explore how private-cloud primitives become a usable Kubernetes foundation. The [Heat repository](https://github.com/farah-ben-harb/openstack-heat-infrastructure) models Neutron networking, Nova compute and Cinder storage; [Ansible automation](https://github.com/farah-ben-harb/k8s-cluster-automation) prepares Linux, containerd, kubeadm and Calico; [Alif manifests](https://github.com/farah-ben-harb/Alif.tn-App-k8s) represent a workload layer. These repositories are intentionally kept as separate architectural components, with validation workflows for templates and automation.

[Heat repository](https://github.com/farah-ben-harb/openstack-heat-infrastructure) · [Kubernetes automation repository](https://github.com/farah-ben-harb/k8s-cluster-automation)

### [Kubernetes Anomaly Detection](https://github.com/farah-ben-harb/kubernetes-anomaly-detection-openstack)

**Problem → build → evidence.** Turn Kubernetes runtime signals into an actionable anomaly signal. I built a FastAPI service that queries Prometheus for CPU, memory and restart data, applies scaling and Isolation Forest detection, and exposes scores through an API and `/metrics`. The current main line includes container hardening, tests and a successful CI run; the service remains a complementary workload rather than an unverified claim of automatic OpenStack integration.

[Repository](https://github.com/farah-ben-harb/kubernetes-anomaly-detection-openstack) · [CI workflow](https://github.com/farah-ben-harb/kubernetes-anomaly-detection-openstack/blob/main/.github/workflows/ci.yml) · [latest observed successful run](https://github.com/farah-ben-harb/kubernetes-anomaly-detection-openstack/actions/runs/43030635364)

### [Azure IaC & CI/CD](https://github.com/farah-ben-harb/flask-azure-devops-pipeline)

**Problem → build → evidence.** Make a Flask service repeatable to test, package and update on an Azure host. I built GitHub Actions validation, Docker packaging, Terraform for an existing Azure VM extension, and an observability path using Prometheus, Grafana, Alertmanager, node_exporter, cAdvisor and blackbox exporter. The repository demonstrates targeted infrastructure automation; it does not claim that Terraform created the VM itself.

[Repository](https://github.com/farah-ben-harb/flask-azure-devops-pipeline) · [CI/CD workflow](https://github.com/farah-ben-harb/flask-azure-devops-pipeline/blob/main/.github/workflows/ci-cd.yml) · [Terraform workflow](https://github.com/farah-ben-harb/flask-azure-devops-pipeline/blob/main/.github/workflows/terraform-azure.yml)

### Other work

[Mini CRM Intelligence](https://github.com/farah-ben-harb/crm-intelligence-mlops) is a separate MLOps lab for synthetic-profile classification with FastAPI, scikit-learn, MLflow, Docker Compose, GitHub Actions and GHCR. AWS is documented there as a learning plan, not as a completed deployment.

## Technical expertise

### 1. Cloud & Infrastructure

Azure · Azure Container Apps · Terraform · OpenStack Heat · Neutron · Nova · Cinder · Ansible · cloud-init · Linux · Bash · networking · IAM concepts

### 2. Platform Engineering & GitOps

Docker · Kubernetes · K3s · kubeadm · containerd · Helm · Argo CD · Kustomize · GitOps · Calico · MetalLB · GHCR · probes/readiness · PVC/local-path

### 3. CI/CD & DevSecOps

GitHub Actions · Jenkins · pytest · Ruff · Gitleaks · Trivy · Semgrep · Bandit · pip-audit · npm audit · immutable image tags · container hardening

### 4. Observability & SRE

Prometheus · Grafana · Alertmanager · ServiceMonitor · health checks · readiness · logging · metrics · incident diagnosis · Dynatrace in professional context

### 5. MLOps & Agentic AI

MLflow Tracking and Registry workflows · FastAPI serving · OpenCV · YOLO11n · ByteTrack · scikit-learn · K-Means · Isolation Forest · RAG · Sentence Transformers · PostgreSQL/pgvector · Ollama in the K3s path · MCP-assisted operations with Claude Desktop in professional context

### 6. Software Engineering & Data

Python · TypeScript · Java · FastAPI · Flask · NestJS · Angular · PostgreSQL · SQLAlchemy · TypeORM · MySQL · REST APIs · n8n · pandas · NumPy

## Engineering evidence

The profile highlights implementation evidence instead of decorative counters:

- **FootballMatch CI:** [workflow](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops/blob/main/.github/workflows/ci.yml) · [successful main run](https://github.com/farah-ben-harb/footballmatch-ai-platform-mlops/actions/runs/43030421510)
- **Kubernetes Anomaly Detection CI:** [workflow](https://github.com/farah-ben-harb/kubernetes-anomaly-detection-openstack/blob/main/.github/workflows/ci.yml) · [successful main run](https://github.com/farah-ben-harb/kubernetes-anomaly-detection-openstack/actions/runs/43030635364)
- **DevSecOps Incident validation:** [Jenkins pipeline](https://github.com/farah-ben-harb/devsecops-incident-platform/blob/main/Jenkinsfile) · [actions history](https://github.com/farah-ben-harb/devsecops-incident-platform/actions)
- **Infrastructure automation:** [Azure CI/CD workflow](https://github.com/farah-ben-harb/flask-azure-devops-pipeline/blob/main/.github/workflows/ci-cd.yml) · [Terraform workflow](https://github.com/farah-ben-harb/flask-azure-devops-pipeline/blob/main/.github/workflows/terraform-azure.yml)

The profile repository also runs a small [integrity workflow](./.github/workflows/profile-integrity.yml) for README links and local assets. It has no cloud credentials, scheduled generators or external publication steps.

## Certifications & education

- **AWS Cloud Practitioner** — AWS · 2024
- **OCI Foundations Associate** — Oracle Cloud Infrastructure · 2024
- **CCNA: Switching, Routing, Wireless** — Cisco · 2023
- **Engineering Cycle in IT Architecture & Cloud Computing** — ESPRIT · expected graduation 2027
- **Engineering path connected to ESIGELEC** — computer engineering, Cloud and Infrastructure focus

## Connect

If you are building cloud platforms, secure delivery systems, Kubernetes reliability practices or MLOps infrastructure, I would be happy to connect.

[![LinkedIn](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/farah-ben-harb-b26845313/)<br>
[Portfolio](https://farah-me.vercel.app) · [Email](mailto:benharbfarah85@gmail.com) · [GitHub](https://github.com/farah-ben-harb) · [Repositories](https://github.com/farah-ben-harb?tab=repositories)
