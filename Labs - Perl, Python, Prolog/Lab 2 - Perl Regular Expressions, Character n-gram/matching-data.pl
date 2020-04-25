 #!/usr/bin/perl
use strict;
use warnings;

sub testre {
my $re = shift;
my $line = shift;
if($line =~ /$re/){
    print "/$re/ MATCH: $'>>>$&<<<$'";
}    
else {
    print "/$re/ NOMATCH: $line";
}
}


while(<DATA>){
    &testre('book', $_);
}

__DATA__
This line has book in it.
How about textbook?
This is capitalized word "BOOK"
