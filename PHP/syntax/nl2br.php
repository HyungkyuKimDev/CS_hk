<?php

/*

nl2br 

=> Inserts HTML line breaks before all newlines in a string
줄 바꿈 코드를 넣음 

nl2br(string $string, bool $use_xhtml = true): string

Returns string with <br /> or <br> inserted before all newlines (\r\n, \n\r, \n and \r).

Ex)

<?php
echo nl2br("foo isn't\n bar");
?>

=>

foo isn't<br />
bar


*/
