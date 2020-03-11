import urllib.request
import random

f = open('url.txt')
urls = []
for line in f.readlines():
    urls.append(line)
random.shuffle(urls)
f.close()

num = len(urls)
print(num)
# test = 150
# train = 500
# valid = 300
# custom remainder

train = int(num / 2 - 150)
valid = int(2 * train / 3)
custom = int(train / 3)
test = num - custom - valid - train


print(f'train {train}')
print(f'valid {valid}')
print(f'test {test}')
print(f'custom {custom}')

print(f'sum {train + valid + test+ custom}')

def download(urlss, folder):
    for i, url in enumerate(urlss):
        try:
            urllib.request.urlretrieve(url, f"{folder}/banana_{i}.jpg")
        except:
            print('oups')

train_url = urls[:train]
valid_url = urls[train:train + valid]
custom_url = urls[train + valid: train + valid + custom]
test_url = urls[train + valid + custom:]

download(train_url, 'train')
download(valid_url, 'valid')
download(custom_url, 'custom')
download(test_url, 'test')
