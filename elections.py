parties = [
    'Action for Israel', 'Bible Bloc', 'Blue and White', 'Da''am–Green Economy–One Nation', 'Human Dignity',
    'Ihud HaBrit VeHaShutafut', 'Jewish Heart', 'Joint List', 'Kama', 'Koah Lehashpi''a', 'Labor–Gesher–Meretz',
    'Liberal–Economic Power', 'Likud', 'Me and You', 'Mishpat Tzedek', 'Mitkademet', 'New Order', 'Otzma Yehudit',
    'Our Israeli Rights', 'Pirate Party', 'Red and White', 'Shama', 'Shas', 'Social Leadership', 'United Torah Judaism',
    'Vision', 'Women''s Voice', 'Yamina', 'Yisrael Beiteinu']

print("My vote goes for: ".join(filter(lambda xy: xy.count("t") == 2 and xy.count("i") == 2, parties)))
