library(tm);
# words added to the tutoiement tag 
tutoiements = c("tu", "te", "ta", "ton", "tes");
tagTu <- content_transformer(function(x) {
    for (i in 1:length(tutoiements)) {
        x = gsub(tutoiements[i],"tagtutoiement", x);
    }
    return (x);
});

