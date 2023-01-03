#!/usr/bin/perl

@files = split(/\n/, `ls -1 src/semantic_llama/evaluation/hpoa/test_cases/*.txt`);
%ids = {};
foreach $file (@files) {
    if ($file =~ m@omim-(\d+)@) {
        $ids{"OMIM:$1"} = 1;
    }
}
while (<>) {
    if (m@^(OMIM:\d+)@) {
        if ($ids{$1}) {
            print;
        }
    }
}
