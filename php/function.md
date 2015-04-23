
## parse_url

parse_url — Parse a URL and return its components

* scheme - e.g. http
* host
* port
* user
* pass
* path
* query - after the question mark ?
* fragment - after the hashmark #


## parse_str

parse_str — Parses the string into variables


Parses str as if it were the query string passed via a URL and sets variables in the current scope.

```
<?php
$str = "first=value&arr[]=foo+bar&arr[]=baz";
parse_str($str);
echo $first;  // value
echo $arr[0]; // foo bar
echo $arr[1]; // baz

parse_str($str, $output);
echo $output['first'];  // value
echo $output['arr'][0]; // foo bar
echo $output['arr'][1]; // baz
```

## array_merge


array_merge — Merge one or more arrays

Merges the elements of one or more arrays together so that the values of one are appended to the end of the previous one. It returns the resulting array.


## http_build_query


http_build_query — Generate URL-encoded query string

Generates a URL-encoded query string from the associative (or indexed) array provided.











