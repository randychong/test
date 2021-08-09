Limbo = "where no balance is"
dantesHashOfInferno = {
  "level1": {
    "name": Limbo,
    "contents": [1, 2, 3, 4, 5, 6, 7, 89, 9, 57, 345, 2, 4123, 4423, 4, 234, 24],
  },
  "level2": {
    "name": "Lust",
    "contents": [12, [56, 56, 56], "swag"],
  },
  "level3": {
    "name": "Gluttony",
    "contents": [{ "volume": 92, "sanctum": "lorem ipsum", "tower": ["crown"] }],
  },
  "level4": {
    "name": "Greed",
    "contents": [{ "fourth": "fourth", "number4": 4 }],
  },
  "level5": {
    "name": "Anger",
    "contents": [
      {
        "reee": 92,
        "reelorum": "latin for ree",
        "reeeeeee": ["angryreeeee", { "anger": "you need to calm down" }],
      },
    ],
  },
  "level6": {
    "name": "Heresy",
    "contents": [],
  },
  "level7": {
    "name": "Violence",
    "contents": [],
  },
  "level8": {
    "name": "Fraud",
    "contents": [],
  },
  "level9": {
    "name": "Treachery",
    "contents": [
      {
        "volume": 92,
        "sanctum": "lorem ipsum",
        "tower": [
          {
            "whywhywhy": 92,
            "reelorum": "latin for ree",
            "ahhhhhh": [
              "angryryyyyyy",
              {
                "anger": "you need to calm down",
                "secret": [
                  { "theSecretIs": "Joe is sorry he gave you this exercise" },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
}

print(dantesHashOfInferno["level1"]["contents"][15])
print(dantesHashOfInferno["level3"]["contents"][0]["tower"][0])
print(dantesHashOfInferno["level5"]["contents"][0]["reeeeeee"][1]["anger"])
print(dantesHashOfInferno["level9"]["contents"][0]["tower"][0]["ahhhhhh"][1]["secret"][0]["theSecretIs"])