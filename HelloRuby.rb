class MegaGreeter
    attr_accessor :names
    def initialize(name="world")
        @names = names
        
    end
    def say_hi
        if @names.nil?
            puts "..."
        elsif @names.respond_to?("each")
            @names.each do |name|
                puts "Hello #{name}"
            end
        else
            puts "Hello #{names}!"
        end
    end
    def say_bye
        if names.nil?
            puts "..."
        elsif @names.respond_to?("join")
            puts "Goodbye #{names.join(",")}"
        else 
            puts "Goodbye #{names}"
        end
    end
end
if __FILE__ == $0
    mg = MegaGreeter.new
    mg.say_hi
    mg.say_bye

    mg.names = "Fred"
    mg.say_hi
    mg.say_bye

    mg.names = ["Albert", "Brenda", "Charles",
              "Dave", "Engelbert"]
    mg.say_hi
    mg.say_bye
end