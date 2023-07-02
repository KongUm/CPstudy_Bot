import os

PREFIX = "!"
TOKEN = os.environ.get("TOKEN")

역할목록 = {
    'CP대회': {
        "embed": {
            "title": "CP 역할",
            "description": "아래 버튼을 눌러 역할을 받아주세요.",
            "color": 0xe9c2c0
        },
        "buttons": [
            {
                "label": "Codeforce & Atcoder",
                "emoji": None,
                "role_id": 1069482542803197962
            },
            {
                "label": "Codeforce",
                "emoji": None,
                "role_id": 1069482132050808884
            },
            {
                "label": "Atcoder",
                "emoji": None,
                "role_id": 1069482345830293567
            },
        ]
    },
}

역할부여_채널_ID = 1125106817450651809
