// Immediately check dark mode preference before page renders to prevent flash
(function() {
  const savedTheme = localStorage.getItem('theme')
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches

  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.classList.add('dark')
  }
})();

// Dark mode toggle functionality
document.addEventListener('DOMContentLoaded', function () {
  const darkModeToggle = document.getElementById('darkModeToggle')
  
  // Show the toggle button after DOM is loaded
  if (darkModeToggle) {
    darkModeToggle.classList.remove('hidden')
  }

  // Toggle dark mode
  darkModeToggle.addEventListener('click', function () {
    document.documentElement.classList.toggle('dark')

    // Save the preference
    const isDark = document.documentElement.classList.contains('dark')
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
  })
})