library(tm);
# words added to the tutoiement tag 
vouvoiements = c("vous", "votre", "vos");
tagVous <- content_transformer(function(x) {
    for (i in 1:length(vouvoiements)) {
        x = gsub(vouvoiements[i],"tagvouvoiement", x);
    }
    return (x);
});

