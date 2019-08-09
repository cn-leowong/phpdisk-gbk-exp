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