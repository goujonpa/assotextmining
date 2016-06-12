library(tm);
# you can add here words to ignore
ignored_words = c("facebook", "www", "http", "https", "com");
ignoredWords <- content_transformer(function(x) {
    for (i in 1:length(ignored_words)) {
        x = gsub(ignored_words[i]," ", x);
    }
    return (x);
});

