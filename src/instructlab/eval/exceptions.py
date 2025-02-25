# SPDX-License-Identifier: Apache-2.0


class EvalError(Exception):
    """
    Parent class for all of instructlab-eval exceptions
    """


class ModelNotFoundError(EvalError):
    """
    Error raised when model is not able to be found

    Attributes
        message     error message to be printed on raise
        path        filepath of model location
    """

    def __init__(self, path) -> None:
        super().__init__()
        self.path = path
        self.message = f"Model could not be found at {path}"


class InvalidGitRepoError(EvalError):
    """
    Error raised when taxonomy dir provided isn't a valid git repo
    Attributes
        message         error message to be printed on raise
        taxonomy_dir    supplied taxonomy directory
    """

    def __init__(self, taxonomy_dir) -> None:
        super().__init__()
        self.taxonomy_dir = taxonomy_dir
        self.message = f"Invalid git repo: {taxonomy_dir}"


class GitRepoNotFoundError(EvalError):
    """
    Error raised when taxonomy dir provided does not exist
    Attributes
        message         error message to be printed on raise
        taxonomy_dir    supplied taxonomy directory
    """

    def __init__(self, taxonomy_dir) -> None:
        super().__init__()
        self.taxonomy_dir = taxonomy_dir
        self.message = f"Taxonomy git repo not found: {taxonomy_dir}"


class InvalidGitBranchError(EvalError):
    """
    Error raised when branch provided is invalid
    Attributes
        message         error message to be printed on raise
        branch          supplied branch
    """

    def __init__(self, branch) -> None:
        super().__init__()
        self.branch = branch
        self.message = f"Invalid git branch: {branch}"


class TasksDirNotFoundError(EvalError):
    """
    Error raised when the tasks dir doesn't exist
    Attributes
        message         error message to be printed on raise
        tasks_dir       tasks dir
    """

    def __init__(self, tasks_dir) -> None:
        super().__init__()
        self.tasks_dir = tasks_dir
        self.message = f"Tasks dir not found: {tasks_dir}"


class InvalidTasksDirError(EvalError):
    """
    Error raised when the tasks dir is invalid
    Attributes
        message         error message to be printed on raise
        tasks_dir       tasks dir
    """

    def __init__(self, tasks_dir) -> None:
        super().__init__()
        self.tasks_dir = tasks_dir
        self.message = f"Invalid Tasks Dir: {tasks_dir}"
