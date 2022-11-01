import random

LANGUAGES = [
    "en",
    "fr",
    "it",
    "es",
    "de",
]

data = [
    ("en", ["tempeval_3"]),
    ("pt", ["timebankpt"]),
    ("fr", ["fr_timebank"]),
    ("it", ["tempeval_2_italian"]),
    ("es", ["spanish_timebank"]),
    ("de", ["krauts"]),

    ("en", ["tempeval_3", "meantime_english", "tcr ancient_time_english", "wikiwars"]),
    ("fr", ["fr_timebank", "ancient_time_french"]),
    ("it", ["tempeval_2_italian", "ancient_time_italian", "meantime_italian", "narrative_container"]),
    ("es", ["spanish_timebank", "tempeval_2_spanish", "meantime_spanish", "ancient_time_spanish"]),
    ("de", ["krauts", "wikiwars_de", "ancient_time_german"]),

    ("en", ["tempeval_3", "meantime_english", "tcr", "ancient_time_english", "wikiwars", "ph_english"]),
    ("pt", ["timebankpt", "ph_portuguese"]),
    ("fr", ["fr_timebank", "ancient_time_french", "ph_french"]),
    ("it", ["tempeval_2_italian", "ancient_time_italian", "meantime_italian", "narrative_container", "ph_italian"]),
    ("es", ["spanish_timebank", "tempeval_2_spanish", "meantime_spanish", "ancient_time_spanish", "ph_spanish"]),
    ("de", ["krauts", "wikiwars_de", "ancient_time_german", "ph_german"]),
]

if __name__ == "__main__":

    for lang, datasets in data:
        random.seed(73)
        n_experiments = 20
        for _ in range(n_experiments):
            dropout = random.choice([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
            trans_hidden_width = random.choice([8, 16, 32, 64, 128, 256])
            trans_maxout_pieces = random.choice([1, 2, 3])
            trans_use_upper = random.choice([True, False])
            embed_width = random.choice([96, 128, 300])
            embed_depth = random.choice(list(range(2, 8)))
            embed_size = random.choice(list(range(2000, 10000, 1000)))
            embed_window_size = random.choice([1, 2])
            embed_maxout_pieces = random.choice([1, 2, 3])

            spacy_cmd = f"python -m src.run " \
                        f"spacy  " \
                        f"--data {' '.join(datasets)} " \
                        f"--language {lang} " \
                        f"--n_epochs 30 " \
                        f"--dropout {dropout} " \
                        f"--trans_hidden_width {trans_hidden_width} " \
                        f"--trans_maxout_pieces {trans_maxout_pieces} " \
                        f"--trans_use_upper {trans_use_upper} " \
                        f"--embed_width {embed_width} " \
                        f"--embed_depth {embed_depth} " \
                        f"--embed_size {embed_size} " \
                        f"--embed_window_size {embed_window_size} " \
                        f"--embed_maxout_pieces {embed_maxout_pieces} "

            print(spacy_cmd)
        print()
    print()
