#!/usr/bin/env ruby

class TextAnalyzer
  attr_accessor :text, :file_path

  def initialize(file_path:, search_word: "")
    @text =  ""
    @file_path = file_path
    load_text_from_file
    @search_word = search_word.downcase
  end

  def command_operation(command)
    case command
      when "-d"
        display_text
      when "-wc"
        display_word_count
      when "-c"
        display_character_count
      when "-l"
        display_line_count
      when "-wt"
        display_top_ten_words
      when "-sc"
        display_specific_word_count
      else
        raise ArgumentError, "Invalid command."
    end
  end

  def display_text
    puts @text
  end

  def display_word_count
    puts @text.split(" ").length
  end

  def display_character_count
    puts @text.gsub("\n", "").length
  end

  def display_line_count
    puts @text.split("\n").length
  end

  def display_top_ten_words
    if @text.empty?
      puts "No text was found in the file."
      return
    end
    if find_top_ten_words == :no_words
      puts "No words were found in the file."
      return
    end
    words, counts = find_top_ten_words
    0.upto(words.length - 1){ |index| puts "#{words[index]}: #{counts[index]}" }
  end

  def display_specific_word_count
    word_count = 0
    @text.downcase.gsub(/[.,:;!?()"]/, "").split().each do |word|
      word_count += 1 if word == @search_word
    end
    puts word_count
  end

  private
  def load_text_from_file
    file_path_validity_check
    @text = File.read(@file_path)
  end

  def file_path_validity_check
    raise LoadError, "No file path." if @file_path == nil
    raise LoadError, "Invalid file format." unless @file_path =~ /\.txt$/
    raise LoadError, "File does not exist." unless File.exist?(@file_path)
  end

  def find_top_ten_words
    words = []
    counts = []

    word_count = each_word_count
    return :no_words if word_count.empty?

    word_count.each do |key, value|
      words.push(key)
      counts.push(value)
      if words.length > 1
        if counts[-1] > counts[-2]
          (words.length - 1).downto(1) do |index|
            if counts[index] > counts[index-1]
              switch_position(words, index)
              switch_position(counts, index)
            else
              break
            end
          end
        end
      end
    end
    output_length = words.length >= 10 ? 9 : words.length - 1
    [words[0..output_length], counts[0..output_length]]
  end

  def each_word_count
    word_count = {}
    @text.downcase.gsub(/[,:;!?()"]/, "").split().each do |word|
      word_count.keys.include?(word) ? word_count[word] += 1 : word_count[word] = 1
    end
    word_count
  end

  def switch_position(array, index)
    temp = array[index-1]
    array[index-1] = array[index]
    array[index] = temp
  end

end

if __FILE__ == $0
  if ARGV.empty?
    puts <<END
< Help >

A program that analyzes text within a file.

Use: [option] [.txt file path]

Options:
[-d]: Display text.
[-wc]: Display word count.
[-c]: Display character count with spaces.
[-l]: Display total line count.
[-wt]: Displays the count of top ten most appearing words.
[-sc] [word]: Displays the number times 'word' appeared within the text
END
    raise ArgumentError, "No arguments passed."
  end

  if ARGV[0] == "-sc"
    raise ArgumentError, "Too many arguments." if ARGV.length > 3
    raise ArgumentError, "Too few arguments." if ARGV.length < 3
  elsif ARGV.length > 2
    raise ArgumentError, "Too many arguments."
  end
  raise ArgumentError, "Too few arguments." if ARGV.length == 1

  if ARGV[0] == "-sc"
    text_analyzer = TextAnalyzer.new(search_word: ARGV[1], file_path: ARGV[2])
  else
    text_analyzer = TextAnalyzer.new(file_path: ARGV[1])
  end
  text_analyzer.command_operation(ARGV[0])
end
