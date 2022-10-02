from os import listdir, getcwd, path
import hashlib

class GetHASH(object):
    def __init__(self, Files, AllFiles, Path, Hash):
        self.Files = Files
        self.AllFiles = AllFiles
        self.Path = Path
        self.Hash = Hash

    def pic(self):
        PicArray = [file for file in self.AllFiles if str(file).startswith(self.Files[0])]
        for file in PicArray:
            hash_md5 = hashlib.md5(open(fr'{self.Path}\{file}', 'rb').read())
            print(f"File name: '{file}', hash: {hash_md5.hexdigest()}")

    def hashfile_pic(self):
        PicArray = [file for file in self.AllFiles if str(file).startswith(self.Files[0])]
        
        for hash in self.Hash:
            Tofile = open(f'picsYY.{hash}', 'w')
            
            match str(hash).split():
                case ['md5']:
                    for file in PicArray:
                        hash_md5 = hashlib.md5(open(fr'{self.Path}\{file}', 'rb').read())
                        Tofile.write(f'{hash_md5.hexdigest()} *{file}\n')
                case ['sha1']:
                    for file in PicArray:
                        hash_sha1 = hashlib.sha1(open(fr'{self.Path}\{file}', 'rb').read())
                        Tofile.write(f'{hash_sha1.hexdigest()} *{file}\n')
                case ['sha256']:
                    for file in PicArray:
                        hash_sha256 = hashlib.sha256(open(fr'{self.Path}\{file}', 'rb').read())
                        Tofile.write(f'{hash_sha256.hexdigest()} *{file}\n')
                case ['sha512']:
                    for file in PicArray:
                        hash_sha512 = hashlib.sha512(open(fr'{self.Path}\{file}', 'rb').read())
                        Tofile.write(f'{hash_sha512.hexdigest()} *{file}\n')
            Tofile.close()
    


    def readme(self):
        FileREADME = [file for file in self.AllFiles if str(file).startswith(self.Files[2])]
        for file in FileREADME:
            hash_sha1_text = hashlib.sha1(open(fr'{self.Path}\{file}', 'rb').read())
            print(f"File name: '{file}', hash (on text): {hash_sha1_text.hexdigest()}")
            
            hash_sha1_binary = hashlib.sha1()
            with open(fr'{self.Path}\{file}', 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha1_binary.update(chunk)
            print(f"File name: '{file}', hash (on binary): {hash_sha1_binary.hexdigest()}")


    def compare_img(self):
        Img = [file for file in self.AllFiles if str(file).startswith(self.Files[1]) and str(file).endswith('.jpg')]
        
        
        hash_in_file = []
        with open(fr'{self.Path}\images.sha1', 'rb') as f:
            Img_sha_1 = f.readlines()
            for sha in Img_sha_1:
                hash_in_file.append(sha.decode('utf-8').replace('*', '').split())
        
        for i in Img:
            for file in hash_in_file:
                if i == file[1]:
                    hash_sha1 = hashlib.sha1(open(fr'{self.Path}\{i}', 'rb').read()).hexdigest()
                    if hash_sha1 == file[0]:
                        print('\033[32m {}'.format(f"File: {i}, matches it's hash (In file: {file[0]}. In hash: {hash_sha1})"))
                    else:
                        print('\033[31m {}'.format(f"File: {i}, does not match it's hash (In file: {file[0]}. In hash: {hash_sha1})"))



if __name__ == "__main__":
    Files = ['pic', 'image', 'README']
    Hash = ['md5', 'sha1', 'sha256', 'sha512']
    Path = fr'{getcwd()}\sums'
    AllFiles = [f for f in listdir(Path) if path.isfile(path.join(Path, f))]
    
    HashClass = GetHASH(Files, AllFiles, Path, Hash)
    print("1. Вычислить md5-хэш файлов pic___.jpg по одному так чтобы результат был выведен на экран.")
    HashClass.pic()
    HashClass.hashfile_pic()
    print("3. Сравнить SHA1-хэш файла README в бинарном и текстовом виде.")
    HashClass.readme()
    print("4. Одной командой проверить SHA1-хэши файлов image___.jpg. Хэши даны в файле images.sha1.")
    HashClass.compare_img()
