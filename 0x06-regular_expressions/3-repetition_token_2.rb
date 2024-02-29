#!/usr/bin/env ruby
matches = ARGV[0].scan(/hbt{2,}n/)
puts matches.join unless matches.empty?
