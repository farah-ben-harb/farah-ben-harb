# Profile maintenance notes

This file records the evidence boundary for the profile README. It is intentionally operational rather than a CV.

## Editing rules

- Keep claims tied to the default branch, a named workflow, a public document or a clearly labelled work branch.
- Describe a configured pipeline as configured unless a public run or runtime validation proves execution.
- Keep `crm-intelligence-mlops` separate; this profile repository does not modify it.
- Do not add contribution graphs, streak counters, generated daily commits or third-party statistics without a reliable fallback.
- Do not add a resume, PDF, resume download or resume preview to the profile README.
- Keep the four local SVGs accessible: every diagram has a title and description and must remain free of scripts or animation.

## Verified snapshot — 11 November 2026

- Profile repository: public, default branch `main`, no workflow existed before this branch.
- Recent successful main-line evidence linked from the README: FootballMatch CI, Kubernetes anomaly detection CI and Mini CRM DevSecOps CI.
- DevoRecruiter has public workflow history including failed runs on `main`; the README therefore describes its delivery controls and repository layout without claiming a green pipeline or production deployment.
- GitHub GraphQL exposed the current six pinned repositories, but not the achievement cards. Pull Shark ×2 and YOLO remain user-reported rather than rendered as copied assets or counters.
- No certification with a public verification link was available in the repository evidence reviewed for this implementation, so no certification gallery is displayed.

## Recommended profile settings (manual)

Profile name: **Farah Ben Harb**

Bio (within GitHub's short bio limit):

> Cloud & DevOps engineer in training | Kubernetes, GitOps, SRE & MLOps

Website: `https://farah-me.vercel.app/`

Recommended pinned repositories:

1. `footballmatch-ai-platform-mlops`
2. `devsecops-incident-platform`
3. `kubernetes-anomaly-detection-openstack`
4. `openstack-heat-infrastructure`
5. `k8s-cluster-automation`
6. `flask-azure-devops-pipeline`

These settings are not changed by the README pull request. Update them from GitHub profile settings after reviewing the proposed order.

## Local validation

Run from the repository root:

```text
python .github/scripts/validate_profile.py
git diff --check
```

The GitHub Actions workflow runs the same deterministic checks on pull requests and pushes to `main`. It does not access cloud resources, call third-party APIs, publish packages or mutate other repositories.
