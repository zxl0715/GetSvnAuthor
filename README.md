# GetSvnAuthor
GetSvnAuthor作用为SVN 迁移到 Git时 需要svn账号与gitlab上账号的关联性文件，程序可以自动生成Author.txt(存储svn账号与gitlab上账号的关联性)

格式: svn用户名 = git用户名，如：

yonghe = yonghe<×××@163.com> 
lihe = lihe<×××@163.com> 


邮箱后缀可以通过 应用程序追加参数，默认后缀为gszh.cn
例如在cmd下执行如下命令：
 getSvnAuthor.exe  163.com