pip install -r requirements.txt

./spider [-rlp] URL
• Option -r : recursively downloads the images in a URL received as a parameter.
• Option -r -l [N] : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.
• Option -p [PATH] : indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.

./scorpion FILE1 [FILE2 ...]