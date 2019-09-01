## Locale Settting Errors

When Your computer isn't set with locale setting it might cause problem such as unable to install python packages

To solve this problem use following code

```shell
$locale-gen en_US.UTF-8
$export LANGUAGE=en_US.UTF-8
$export LANG=en_US.UTF-8
$export LC_ALL=en_US.UTF-8
$locale-gen en_US.UTF-8
$dpkg-reconfigure locales
```
