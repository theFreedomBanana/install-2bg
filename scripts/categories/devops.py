"""DevOps tool selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Chef Workstation (Linux only)", "value": "chef"},
    {"name": "Docker (CLI, with Colima on macOS)", "value": "docker"},
    {"name": "Docker Compose", "value": "docker-compose"},
    {"name": "Grafana", "value": "grafana"},
    {"name": "Helm", "value": "helm"},
    {"name": "Kind", "value": "kind"},
    {"name": "Kubectl", "value": "kubectl"},
    {"name": "K9s", "value": "k9s"},
    {"name": "Lens", "value": "lens"},
    {"name": "Minikube", "value": "minikube"},
    {"name": "Podman", "value": "podman"},
    {"name": "Prometheus", "value": "prometheus"},
    {"name": "Pulumi", "value": "pulumi"},
    {"name": "Terraform", "value": "terraform"},
    {"name": "Terragrunt", "value": "terragrunt"},
]


def select_devops():
    """Display a multi-select menu for DevOps tools."""

    return choose("Which DevOps tools would you like to install?", CHOICES)
