engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

zin = input("Geef een zin in het engels: ")
lijst_gesplitst = zin.split()
for woord in lijst_gesplitst:
    if woord in engels_nederlands:
        nederlands =engels_nederlands.get(woord, 1)
        locatie = lijst_gesplitst.index(woord)
        lijst_gesplitst.remove(woord)
        lijst_gesplitst.insert(locatie, nederlands)
zin = " ".join(lijst_gesplitst)
print(zin)