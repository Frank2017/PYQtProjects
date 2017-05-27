# coding=UTF-8
import sys
import os
import cPickle
import funclibs

class FileModel:
    def __init__(self):
        # 运行程序的当前路径
        self.CUR_DIR = os.path.curdir
        # 密码本所在的文件夹路径，程序所在目录下新建PswBooksDB文件夹
        self.PSWBOOKSDIR = os.path.join(self.CUR_DIR,'PswBooksDB')
        # 密码本管理文件的文件名
        self.PSWBOOKSMANAGENAME = 'pswbooks'

        pass
    def initModel(self):
        # 初始化密码管理文件
        self.__initPswBooksManage()
        # 密码本管理文件读取
        self.PswBooksDict = self.__read(self.PSWBOOKSMANAGENAME, self.CUR_DIR)
        if self.PswBooksDict is None:
            return 0
        # 初始化密码本库文件夹
        self.__initPswBooksDir()
        return 1
        pass
    def __initPswBooksManage(self):
        # 如果文件不存在先写入密码本管理文件
        if not os.path.exists(os.path.join(self.CUR_DIR, self.PSWBOOKSMANAGENAME)):
            Dict = {}
            self.__write(Dict, self.PSWBOOKSMANAGENAME, self.CUR_DIR)
        pass

    def __initPswBooksDir(self):
        # 如果密码本库文件夹不存在，创建该文件夹
        if not os.path.exists(self.PSWBOOKSDIR):
            os.mkdir(self.PSWBOOKSDIR)
        pass

    def __read(self,name,path):
        """
        内部使用接口，读取path下，name文件
        :param name: 文件名
        :param path: 文件路径
        :return: 返回读取的dict对象
        """
        file = os.path.join(path, name)
        try:
            fp = open(file, 'r')
            data = cPickle.load(fp)
            return data
        except:
            return None
        pass

    def __write(self,data,fname,path):
        """
        内部使用接口，将data写入path下的，fname的文件中，fname无后缀，但是存储的是cPickle文件
        :param data: 写入数据，为dict
        :param fname: 写入文件名
        :param path: 写入文件的路径
        """
        file = os.path.join(path, fname)
        try:
            fp = open(file, 'w')
            cPickle.dump(data, fp)
        except:
            return None
        pass

    def setPswBooksManage(self,data):
        if not os.path.exists(os.path.join(self.CUR_DIR, self.PSWBOOKSMANAGENAME)):
            self.__initPswBooksManage()
        self.__write(data,self.PSWBOOKSMANAGENAME,self.CUR_DIR)
        pass

    def setPswBook(self,data,fname):
        if not os.path.exists(self.PSWBOOKSDIR):
            self.__initPswBooksDir()
        self.__write(data, fname, self.PSWBOOKSDIR)
        pass

    def getPswBooksManage(self):
        """
        获取密码本管理文件（外部使用接口）
        :return: 返回密码本管理文件dict对象
        """
        if os.path.exists(os.path.join(self.CUR_DIR, self.PSWBOOKSMANAGENAME)):
            return self.__read(self.PSWBOOKSMANAGENAME,self.CUR_DIR)
        else:
            return None

    def getPswBook(self,fname):
        """
        外部接口，获取fname对应的密码本
        :param fname: 以.pkl为后缀的文件，文件名是密码本的MD5校验字符串
        :return: 
        """
        # 若fname的文件存在返回读取的dict对象，若不存在返回None
        if os.path.exists(os.path.join(self.PSWBOOKSDIR,fname)):
            return self.__read(fname,self.PSWBOOKSDIR)
        else:
            return None
        pass
    
    def removePswFile(self, fname):
        fpath = os.path.join(self.PSWBOOKSDIR, fname)
        if os.path.exists(fpath):
            os.remove(fpath)
            return 1
        else:
            # 删除失败
            if os.path.exists(fpath):
                return 0
            # 文件不存在
            else:
                return -1
        pass

    def renamePswFile(self, oldName, newName):
        oldFile = os.path.join(self.PSWBOOKSDIR, oldName)
        newFile = os.path.join(self.PSWBOOKSDIR, newName)
        if os.path.exists(oldFile):
            # 新命名的文件存在
            if os.path.exists(newFile):
                return -2
            else:
                try:
                    os.rename(oldFile, newFile)
                    return 1
                except:
                    return 0
        else:
            return -1

    def pswFileExist(self,fname):
        return os.path.exists(os.path.join(self.PSWBOOKSDIR, fname))

    def manageFileExist(self,fname):
        return os.path.exists(os.path.join(self.CUR_DIR, self.PSWBOOKSMANAGENAME))

if __name__ == '__main__':
    file = FileModel()
    # dict = {'liulei':'male','hah':'female'}
    # file.setPswBooksManage(dict)
    # dict2 = {'liulei':'male','hah':'female', 'lala':'fuck'}
    # file.setPswBooks(dict2, funclibs.getMD5('密码本一'))
    # print file.getPswBooksManage()
    # print file.getPswBook(funclibs.getMD5('密码本一'))
    # print file.__read()