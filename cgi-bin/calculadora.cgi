#!/usr/bin/perl

use strict;
use warnings;

use CGI;
my $cgi = CGI->new;

print $cgi->header;

my $expresion = $cgi->param('expresion');

if ($expresion) {
    # Verifica si la expresión es segura usando expresiones regulares
    if ($expresion =~ /^(\d+(\.\d+)?)[+\-*/]\d+(\.\d+)?$/) {
        eval {
            my $resultado = eval $expresion;
            die "Error en la expresión: $@" if $@;

            print "<p>Resultado: $resultado</p>";
        };
        if ($@) {
            print "<p>Error en la expresión: $@</p>";
        }
    } else {
        print "<p>Expresión no válida.</p>";
    }
} else {
    print "<p>Ingresa una expresión.</p>";
}