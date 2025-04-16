COMMIT_TYPES = {
    "feat": {
        "keywords": ["add", "create", "implement", "introduce", "new feature"],
        "description": "New features"
    },
    "fix": {
        "keywords": ["fix", "resolve", "bug", "error", "issue"],
        "description": "Bug fixes"
    },
    "docs": {
        "keywords": ["readme", "doc", "documentation", "comment"],
        "description": "Documentation changes"
    },
    "style": {
        "keywords": ["format", "lint", "rename variable", "indent"],
        "description": "Code style changes (not affecting logic)"
    },
    "refactor": {
        "keywords": ["refactor", "restructure", "simplify", "clean code"],
        "description": "Code changes without fixing bugs or adding features"
    },
    "test": {
        "keywords": ["test", "unittest", "pytest", "assert", "mock"],
        "description": "Test-related changes"
    },
    "chore": {
        "keywords": ["remove", "update config", "cleanup", "maintenance"],
        "description": "Routine tasks and maintenance"
    },
    "build": {
        "keywords": ["build", "dependency", "package", "requirement.txt"],
        "description": "Build system or dependency changes"
    },
    "ci": {
        "keywords": ["ci", "github actions", "workflow", "pipeline"],
        "description": "Continuous Integration configuration changes"
    },
    "perf": {
        "keywords": ["performance", "optimize", "speed", "improve loop"],
        "description": "Performance improvements"
    },
    "revert": {
        "keywords": ["revert", "undo"],
        "description": "Reverting previous changes"
    },
    "security": {
        "keywords": ["security", "vulnerability", "injection", "encrypt", "sanitize"],
        "description": "Security improvements"
    }
}