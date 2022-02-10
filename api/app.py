import os
from flask import Flask, jsonify
from flask_cors import CORS
from src.services.get_commit_by_hexsha import GetCommitByHexsha
from src.repositories.branch_repository import BranchRepository
from src.services.get_branches import GetBranches

from src.services.get_commits_by_branch import GetCommitsByBranch
from src.repositories.commit_repository import CommitRepository

from src.repositories.author_repository import AuthorRepository

app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "http://localhost:8080"}})

path = os.getcwd()

@app.route('/')
def hello_world():
    return path

# get all branches
@app.route('/branches')
def branches():
    branches = GetBranches(BranchRepository(path=path))
    return jsonify({
        "data": branches.execute(),
        "message": "success!"
    }), 202

# get all commits by branch name
@app.route('/branches/<string:branch_name>/commits')
def commits_by_branch(branch_name):
    try:
        commits = GetCommitsByBranch(CommitRepository(path=path))
        return jsonify({
            "data": commits.execute(branch_name),
            "message": "success!"
        }), 202
    except Exception as e:
        return jsonify({
            "message": str(e),
            "data": []
        }), 404

# get commit by hexsha
@app.route('/commits/<string:hexsha>')
def commits_by_hexsha(hexsha):
    try:
        commit = GetCommitByHexsha(CommitRepository(path=path))
        return jsonify({
            "data": commit.execute(hexsha),
            "message": "success!"
        }), 202
    except Exception as e:
        return jsonify({
            "message": str(e),
            "data": []
        }), 404


@app.route('/authors')
def authors():
    try:
        get_authors = AuthorRepository()
        return jsonify({
            "data": get_authors.get_authors(),
            "message": "success!"
        }), 202
    except Exception as e:
        return jsonify({
            "message": str(e),
            "data": []
        }), 404

if __name__ == '__main__':
    app.run(debug=True, port=4040)