#!/usr/bin/perl

use strict;
use warnings;

use CGI;
my $cgi = CGI->new;

print $cgi->header;

my $expresion = $cgi->param('expresion');

# Verifica si la expresión contiene solo números y operadores permitidos
if ($expresion =~ /^(\d+(\.\d+)?)[+\-*/]\d+(\.\d+)?$/) {
    my $resultado = eval $expresion;

    if (defined $resultado) {
        print "<p>Resultado: $resultado</p>";
    } else {
        print "<p>Error en la expresión.</p>";
    }
} else {
    print "<p>Expresión no válida.</p>";
}