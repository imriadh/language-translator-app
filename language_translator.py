# !pip install deep_translator
from deep_translator import GoogleTranslator

def display_main_menu(default_from, default_to):
    print("\n========= Translator Options =========")
    print(f"Default From Language [{default_from}] -> Default To Language [{default_to}]")
    print("  1. Quick translate (using default languages)")
    print("  2. Print available languages")
    print("  3. Change default languages")
    print("  4. Translate (detect source language)")
    print("  5. Translate (specify languages)")
    print("  6. Manage Favorites")
    print("  0. Quit")

def translate(from_lang, to_lang, text_to_translate):
    return GoogleTranslator(source=from_lang, target=to_lang).translate(text_to_translate)

def quick_translate(from_lang, to_lang):
    text_to_translate = input("Text to translate: ")
    translation = translate(from_lang, to_lang, text_to_translate)

    print(f"\n++++++++++++++++ Translation ++++++++++++++++")
    print(translation)

def print_available_languages():
    print("+++++++++++++ Available Languages +++++++++++++")
    available_languages = GoogleTranslator().get_supported_languages(as_dict=True)
    for lang, abbr in available_languages.items():
        print(f"\t{lang}: {abbr}")

def set_default_languages():
    from_lang = input("New default from language: ").lower()
    to_lang = input("New default to language: ").lower()

    print("\n+++++++++++++ Default Languages Updated +++++++++++++")
    print(f"From [{from_lang}] -> To [{to_lang}]")

    return from_lang, to_lang

def translate_detect_source_lang():
    to_lang = input("Language to translate to: ")
    quick_translate('auto', to_lang)

def translate_specify_langs():
    from_lang = input("Language to translate from: ")
    to_lang = input("Language to translate to: ")

    quick_translate(from_lang, to_lang)

def display_favorites_menu():
    print("\n********* Favorites Options *********")
    print("  1. Add favorite")
    print("  2. Remove favorite")
    print("  3. Edit favorite")
    print("  4. Print favorites")
    print("  0. Quit managing favorites")

def manage_favorites(favorites):
    should_continue = True

    while should_continue:
        display_favorites_menu()
        try:
            action = int(input("Enter an option number: "))
        except ValueError:
            print("\n========= Error =========")
            print("Please enter a number.")
            continue
        else:
            print("************************************\n")

        if action == 0:
            should_continue = False
        elif action == 1:
            favorites = add_favorite(favorites)
        elif action == 2:
            favorites = remove_favorite(favorites)
        elif action == 3:
            favorites = edit_favorite(favorites)
        elif action == 4:
            print_favorites(favorites)
        else:
            print("\n========= Invalid Option =========")
            print("Enter a number between 0 and 4.\n")

    return favorites

def add_favorite(favorites):
    text_to_favorite = input("Enter text to favorite: ")
    from_lang = input("Language to translate from: ")
    to_lang = input("Language to translate to: ")

    translation = translate(from_lang, to_lang, text_to_favorite)
    favorites[text_to_favorite] = {"from_lang": from_lang, "to_lang": to_lang, "translation": translation}

    print("\n+++++++++++++++ Added to Favorites +++++++++++++++")
    print(f"{text_to_favorite} -> {translation}")

    return favorites

def remove_favorite(favorites):
    favorite_to_remove = input("Favorite to remove: ")

    if favorite_to_remove in favorites:
        favorites.pop(favorite_to_remove)
        print("\n+++++++++++++++ Removed Favorite +++++++++++++++")
        print(f"Removed: {favorite_to_remove}")
    else:
        print("\n+++++++++++++++ Error +++++++++++++++")
        print(f"{favorite_to_remove} not found in favorites.")

    return favorites

def edit_favorite(favorites):
    favorite_to_edit = input("Favorite to edit: ")

    if favorite_to_edit in favorites:
        to_lang = input(f"New 'to' language (current: {favorites[favorite_to_edit]['to_lang']}): ")

        translation = translate(favorites[favorite_to_edit]['from_lang'], to_lang, favorite_to_edit)
        favorites[favorite_to_edit].update({'to_lang' : to_lang, 'translation' : translation})

        print("\n+++++++++++++++ Updated Favorite +++++++++++++++")
        print(f"{favorite_to_edit} -> {translation}\n")
    else:
        print("\n+++++++++++++++ Error +++++++++++++++")
        print(f"{favorite_to_edit} not found in favorites.")

    return favorites

def print_favorites(favorites):
    if favorites:
        print("\n+++++++++++++++ Favorites +++++++++++++++")
        for favorite, details in favorites.items():
            print(f"\t{favorite}: {details['translation']} (from {details['from_lang']} to {details['to_lang']})")
    else:
        print("\n+++++++++++++++ Error +++++++++++++++")
        print("No favorites saved.")

# Main program
if __name__ == "__main__":
    default_from = "en"
    default_to = "es"
    should_continue = True
    favorites = {}

    while should_continue:
        display_main_menu(default_from, default_to)
        try:
            action = int(input("Enter an option number: "))
        except ValueError:
            print("\n========= Error =========")
            print("Please enter a number.")
            continue
        else:
            print("====================================\n")

        if action == 0:
            should_continue = False
        elif action == 1:
            quick_translate(default_from, default_to)
        elif action == 2:
            print_available_languages()
        elif action == 3:
            default_from, default_to = set_default_languages()
        elif action == 4:
            translate_detect_source_lang()
        elif action == 5:
            translate_specify_langs()
        elif action == 6:
            favorites = manage_favorites(favorites)
        else:
            print("========= Invalid Option =========")
            print("Enter a number between 0 and 6.")
