console.log("salut");
window.onload = function() {
// Cette fonction s'exécutera lorsque la page sera entièrement chargée

// Récupérer le contenu de l'article
const articleContent = "{{ article_data.contenu }}"

// Insérer le contenu de l'article dans la balise avec l'ID 'article-post'
document.getElementById('article-post').insertAdjacentHTML('beforeend', articleContent);
}