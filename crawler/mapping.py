TECHNOLOGY_RELATIONS = {
    "php": [
        "laravel", "symfony", "composer", "dockerfile", "phpunit"
    ],
    "laravel": [
        "mysql", "redis", "eloquent", "blade", "livewire", "laravel-mix", "laravel-echo", "laravel-valet",
        "passport", "vue", "react", "lighthouse"
    ],
    "lighthouse": [
        "graphql", "eloquent", "laravel", "api", "api-client"
    ],
    "eloquent": ["mysql", "sqlite", "mssql", "sqlserver", "oracle", "cockroachdb", "tidb", "sql"],
    "python": ["django", "flask", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "dockerfile", "sql"],
    "django": ["postgresql", "django-orm", "django-rest-framework", "dockerfile"],
    "django-orm": ["postgresql", "mysql", "sqlite", "mssql", "sqlserver", "oracle", "cockroachdb", "tidb", "sql"],
    "java": ["spring", "hibernate", "maven", "dockerfile"],
    "spring": ["mssql", "springboot", "thymeleaf"],
    "ruby": ["rails"],
    "rails": ["sqlite", "activerecord"],
    "javascript": [
        "nodejs", "react", "vue", "angular", "typescript", "dockerfile", "npm", "yarn", "jss"
    ],
    "jss": ["css"],
    "nodejs": ["express", "mongoose", "npm", "yarn", "dockerfile", "typescript", "typeorm"],
    "react": ["redux", "javascript", "dockerfile"],
    "go": ["gin", "beego", "echo", "gorm", "grpc", "golang", "dockerfile"],
    "gorm": ["mysql", "postgresql", "sqlite", "mssql", "sqlserver", "oracle", "cockroachdb", "tidb", "sql"],
    "html": ["css", "javascript"],
    "typescript": ["angular", "react", "vue", "webpack", "npm", "yarn", "dockerfile", "sql", "dockerfile"],
    "css": ["scss", "sass", "less", "bootstrap"],
    "c": ["linux", "windows", "maxos", "bash", "c++", "dockerfile"],
    "c++": ["linux", "windows", "maxos", "qt", "boost", "dockerfile"],
    "rust": ["linux", "windows", "maxos", "cargo", "wasm", "dockerfile"],

    # DevOps & Cloud
    "dockerfile": ["docker", "docker-compose"],
    "docker": ["kubernetes", "docker-compose", "dockerfile", "docker-swarm", "docker-hub"],
    "kubernetes": ["helm", "istio", "kubeflow", "k3s", "kubectl", "yaml"],
    "aws": ["ec2", "s3", "lambda"],
    "azure": ["azure-functions", "azure-web-apps"],
    "gcp": ["gce", "gcs"],
    "cicd": ["jenkins", "travis-ci", "github-actions", "gitlab-ci", "circleci", "teamcity", "bamboo", "gocd"],

    # Data Science & ML
    "r": ["shiny", "dplyr", "ggplot2"],
    "jupyter-notebook": ["pandas", "numpy", "scikit-learn", "tensorflow", "pytorch"],

    # Mobile development
    "android": ["kotlin", "java", "android-studio"],
    "ios": ["swift", "objective-c", "cocoa-touch", "xcode"],

    # System programming & OS
    "linux": ["bash", "zsh", "shell", "systemd", "debian", "ubuntu", "centos", "redhat", "archlinux", "gentoo"],
    "macos": ["zsh", "shell", "ios", "swift", "objective-c", "homebrew", "macos-catalina"],

    # Databases
    "databases": ["postgresql", "mysql", "sqlite", "mssql", "sqlserver", "oracle", "cockroachdb", "tidb", "sql"],

    # Linux
    "deb": ["linux", "debian", "ubuntu", "linuxmint", "kali-linux", "raspbian", "raspberryos", "elementaryos"],
    "rpm": ["linux", "redhat", "centos", "almalinux", "rockylinux", "fedora"],
    "arch": ["linux", "archlinux"],
    "gentoo": ["linux"],
    "alpine": ["linux"],
    "repository": ["git", "cvs", "svn", "mercurial", "github", "gitlab", "bitbucket"],
    "thin-client": ["virtualization", "vdi", "cloud"],

    # Backend programming
    "api": [
        "rest", "restful", "graphql", "grpc", "soap", "json", "xml", "openapi", "swagger", "laravel", "django", "flask",
        "spring", "nodejs", "express", "gin", "beego", "php", "java", "python", "ruby"
    ],
    "api-client": [
        "rest", "rest", "graphql", "grpc", "soap", "json", "xml", "openapi", "swagger", "laravel", "django",
        "flask"
    ],

}
CLUSTERS = {
    "devops": [
        "docker", "kubernetes", "jenkins", "travis-ci", "github-actions", "aws", "azure", "gcp", "terraform",
        "ansible", "cicd"
    ],
    "data-science": [
        "python", "r", "jupyter", "jupyter-notebook", "jupyterlab", "tensorflow", "pytorch", "pandas", "numpy",
        "scikit-learn"
    ],
    "system-programming": [
        "c", "c++", "rust", "asm"
    ],
    "system-administration": [
        "linux", "shell", "bash", "systemd", "perl"
    ],
    "machine-learning": [
        "data-science", "python", "tensorflow", "pytorch", "keras", "fastai", "scikit-learn", "opencv",
        "pandas", "numpy", "scipy", "tensorflowjs", "tensorboard", "jupyter", "jupyter-notebook",
        "jupyterlab", "kaggle", "matplotlib", "seaborn", "plotly", "bokeh", "dash", "streamlit", "mlflow",
        "pycaret", "xgboost", "lightgbm", "catboost", "h2o", "shap", "eli5", "lime", "scikit-optimize",
        "hyperopt", "optuna", "ml-agents", "ray", "horovod", "pytorch-lightning", "pytorch-ignite",
        "llm", "pytorch-geometric", "pytorch-forecasting", "pytorch-tabnet", "pytorch3d", "pytorchvideo",
    ],
    "web-development": [
        "html", "css", "javascript", "php", "java", "python", "ruby", "django", "flask", "spring", "nodejs",
    ],
    "ios-development": [
        "ios", "swift", "objective-c", "cocoa-touch", "xcode",
    ],
    "android-development": [
        "android", "kotlin", "java", "android-studio", "flutter", "react-native", "gradle", "kotlin-android",
    ],
    "1c-development": [
        "1c", "1c-bitrix", "1c-enterprise", "windows", "linux", "system-administration", "postgresql", "shell",
    ],
}