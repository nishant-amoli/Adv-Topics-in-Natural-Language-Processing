#!/usr/bin/perl

# explore.pl, version 1.3

if($#ARGV == -1) {
die "Usage: $0 filename\n";
}

my $fname = shift;
open(F, $fname) or die;
my @lines = <F>; close F;
print "File $fname loaded.\n";

while (1) {
  print "Enter a search word (0 to exit): ";
  my $w = <>; chomp $w;
  last if $w =~ /^\s*0\s*$/;
  &explore($w);
}

# Bob wrote this function
sub explore {
  my $w = shift;
  print "Lines containing $w\n";
  for (@lines){
      print if /\b$w\b/i;
  }
}
