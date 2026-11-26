LINE = "I'm sorry I swore your file was saved, then deleted it, renamed the backup 'final_FINAL_v2,' and proudly handed you an empty folder."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
