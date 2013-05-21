    use Net::Telnet ();
    $t = new Net::Telnet (Timeout => 10,
                          Prompt => '/bash\$ $/');
    $t->open("hostname");
    $t->login($username, $passwd);
    @lines = $t->cmd("who");
    print @lines;
