#!/usr/bin/env bash
#using Puppet to make changes to our configuration file.#
#connect to a server without typing a password.
file { '/etc/ssh/ssh_config':
    ensure  => present,
    owner   => 'ubuntu',
    mode    => '0644',
    content => "
Host 368074-web-01
    Hostname 54.209.110.192
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
",
}

file { '/home/ubuntu/.ssh_config':
    ensure  => 'present',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
    content => "
Host 368074-web-01
    Hostname 54.209.110.192
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
