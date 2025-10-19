# 🌐 Language Translator App

A powerful and user-friendly command-line language translation application built with Python, leveraging Google Translate API through the `deep_translator` library.

## ✨ Features

- **Quick Translation**: Translate text instantly using default language settings
- **Auto-Detection**: Automatically detect source language for seamless translation
- **Custom Language Selection**: Choose specific source and target languages
- **Favorites Management**: Save, edit, and manage your frequently used translations
- **100+ Languages Supported**: Access to all languages supported by Google Translate
- **User-Friendly Interface**: Interactive menu-driven interface for easy navigation

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features Overview](#features-overview)
- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/language-translator-app.git
cd language-translator-app
```

2. Install required dependencies:
```bash
pip install deep_translator
```

3. Run the application:
```bash
python language_translator.py
```

## 💻 Usage

### Main Menu Options

When you run the application, you'll see the following menu:

```
========= Translator Options =========
Default From Language [en] -> Default To Language [es]
  1. Quick translate (using default languages)
  2. Print available languages
  3. Change default languages
  4. Translate (detect source language)
  5. Translate (specify languages)
  6. Manage Favorites
  0. Quit
```

### Quick Start Example

1. **Quick Translation** (Option 1):
   - Enter text in the default source language (English)
   - Get instant translation to the default target language (Spanish)

2. **View Available Languages** (Option 2):
   - Display all supported languages with their abbreviations

3. **Change Default Languages** (Option 3):
   - Set your preferred default source and target languages

4. **Auto-Detect Translation** (Option 4):
   - Let the app automatically detect the source language
   - Specify only the target language

5. **Custom Translation** (Option 5):
   - Specify both source and target languages manually

6. **Manage Favorites** (Option 6):
   - Add frequently used translations
   - Edit existing favorites
   - Remove unwanted favorites
   - View all saved favorites

## 🎯 Features Overview

### 1. Quick Translate
Translate text using predefined default languages for faster workflow.

### 2. Language Detection
Automatically detect the source language - perfect when you're unsure of the input language.

### 3. Favorites System
- **Add**: Save translations you use frequently
- **Edit**: Update target language for saved translations
- **Remove**: Delete translations you no longer need
- **View**: Display all your saved favorites with details

### 4. Comprehensive Language Support
Access to 100+ languages including:
- English, Spanish, French, German, Italian
- Chinese, Japanese, Korean, Hindi, Arabic
- And many more!

## 📦 Requirements

```
deep_translator>=1.9.0
```

## 🔧 How It Works

The application uses the `deep_translator` library which provides a clean interface to Google Translate API:

1. **Translation Engine**: Powered by `GoogleTranslator` class
2. **Language Detection**: Uses 'auto' mode to detect source language
3. **Data Storage**: Favorites stored in-memory (dictionary structure)
4. **User Interface**: Menu-driven CLI for intuitive interaction

### Code Structure

- **Main Menu Loop**: Controls the primary application flow
- **Translation Functions**: Handle different translation scenarios
- **Favorites Management**: Complete CRUD operations for saved translations
- **Error Handling**: Validates user input and handles exceptions gracefully

## 🌟 Example Use Cases

### Scenario 1: Travel Preparation
- Set default languages (English → Spanish)
- Save common phrases as favorites
- Quick translate phrases on the go

### Scenario 2: Language Learning
- Translate words and phrases
- Save vocabulary in favorites
- Review translations later

### Scenario 3: Multilingual Communication
- Use auto-detect for incoming messages
- Translate to various languages
- Maintain a library of common translations

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Future Enhancement Ideas

- [ ] Export favorites to JSON/CSV
- [ ] Persistent storage for favorites (database)
- [ ] Translation history
- [ ] Batch translation from file
- [ ] GUI interface
- [ ] Voice input/output support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**RIAD**

## 🙏 Acknowledgments

- [deep_translator](https://github.com/nidhaloff/deep-translator) - For providing the translation API wrapper
- Google Translate - For the translation engine
- Python Community - For continuous support and inspiration

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Contact: your.email@example.com

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Note**: This application requires an internet connection to perform translations as it uses Google Translate API through the `deep_translator` library.
