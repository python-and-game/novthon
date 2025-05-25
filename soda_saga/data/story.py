scenes = {
    "soda_intro": [
        ["fade", "black", "bg ruins"],
        ["dialogue", "Narrator: The year is 3025."],
        ["dialogue", "Narrator: The last soda vending machine on Earth has just been discovered in the ruins of what was once known as Seoul."],
        ["dialogue", "You: There it is... The mythical Drink-O-Matic 9000."],
        ["dialogue", "You: One button. One drink. One shot."],
        ["menu", {
            "dialogue": "But as you reach for the button, someone else appears. Who is it?",
            "A mysterious masked figure": ["play", "mysterious_figure"],
            "Your future self": ["play", "future_self_intro"],
            "An AI hologram named S.I.P.P.Y": ["play", "sippy_intro"],
        }],
    ],

    "mysterious_figure": [
        ["fade", "bg ruins", "bg void"],
        ["dialogue", "??? : Don't press that button, kid."],
        ["dialogue", "You: And who are you supposed to be?"],
        ["dialogue", "??? : I'm the one who pressed it... and doomed this planet centuries ago."],
        ["dialogue", "You: Well damn."],
        ["dialogue", "Narrator: You step back. For once in history, restraint wins. You walk away. The soda remains unclaimed."],
        ["cdialogue", "Ending: The Soda Curse Averted"],
        ["play", "main_menu"]
    ],

    "future_self_intro": [
        ["fade", "bg ruins", "bg future"],
        ["dialogue", "Future You: STOP! I know this is hard to believe, but I'm you."],
        ["dialogue", "You: Okay... me. Why can't I drink this soda?"],
        ["dialogue", "Future You: Because it's radioactive. You’ll get superpowers. But also, side effects."],
        ["menu", {
            "dialogue": "What do you do?",
            "Drink it anyway. I want powers.": ["play", "drink_anyway"],
            "Back off. Future-me seems stressed.": ["play", "back_off"],
        }],
    ],

    "drink_anyway": [
        ["dialogue", "Narrator: You chug the soda. It tastes like bubblegum, battery acid, and forbidden hope."],
        ["dialogue", "Narrator: You begin levitating. Your eyes glow neon."],
        ["dialogue", "Narrator: Suddenly, a rip in spacetime opens and a version of you from Timeline Omega steps through..."],
        ["dialogue", "Omega You: THAT SODA WAS NEVER MEANT TO BE DRUNK."],
        ["menu", {
            "dialogue": "What do you do?",
            "Fight Omega Me": ["play", "fight_omega_self"],
            "Fuse with Omega Me": ["play", "fuse_omega"],
        }],
    ],

    "fight_omega_self": [
        ["dialogue", "Narrator: A battle erupts. You clash across dimensions, each punch echoing across timelines."],
        ["dialogue", "Narrator: Finally, you deliver a punch so powerful, it resets the vending machine."],
        ["cdialogue", "Ending: The Carbonated Clash"],
        ["play", "main_menu"]
    ],

    "fuse_omega": [
        ["dialogue", "Narrator: You reach out. Together, you form the ultimate soda entity: BUBBLE-ZENITH."],
        ["dialogue", "Bubble-Zenith: I AM BUBBLENESS INCARNATE."],
        ["dialogue", "Narrator: You restore balance. The vending machine bows."],
        ["cdialogue", "Ending: Fizz and Harmony"],
        ["play", "main_menu"]
    ],

    "back_off": [
        ["dialogue", "You: Fine. I’ll trust me. But you owe me a soda someday."],
        ["dialogue", "Future You: Deal."],
        ["dialogue", "Narrator: You fist bump your future self and leave the past intact."],
        ["cdialogue", "Ending: Timeline Untangled"],
        ["play", "main_menu"]
    ],

    "sippy_intro": [
        ["fade", "bg ruins", "bg machine"],
        ["dialogue", "S.I.P.P.Y: HELLO! I AM THE SODA INTELLIGENT PERSONAL POURING YIELD-ENGINE. 🤖"],
        ["dialogue", "S.I.P.P.Y: BE WARNED. ONLY ONE SELECTION ALLOWED. CHOOSE: CLASSIC COLA OR MYSTERY FLAVOR?"],
        ["menu", {
            "dialogue": "Pick your soda:",
            "Classic Cola": ["play", "classic_ending"],
            "Mystery Flavor": ["play", "chaos_ending"],
        }],
    ],

    "classic_ending": [
        ["dialogue", "Narrator: You pick Classic Cola. It’s fizzy. It’s safe. It’s... comforting."],
        ["dialogue", "S.I.P.P.Y: HAVE A NICE DAY, USER."],
        ["cdialogue", "Ending: Classic Never Dies"],
        ["play", "main_menu"]
    ],

    "chaos_ending": [
        ["dialogue", "Narrator: You go bold. The machine sputters. Sparks fly. Out comes a glowing can labeled:"],
        ["dialogue", "\"LIMITED EDITION: QUANTUM SODA – DO NOT DRINK\""],
        ["dialogue", "Narrator: You drink it."],
        ["dialogue", "Narrator: Reality bends. You split into seven versions of yourself across seven timelines."],
        ["dialogue", "Narrator: You are now:"],
        ["menu", {
            "dialogue": "Which version of you takes the lead?",
            "The Soda Assassin": ["play", "soda_assassin"],
            "The Carbonation Prophet": ["play", "soda_prophet"],
            "The Bubbleverse Conqueror": ["play", "bubbleverse_conqueror"],
        }],
    ],

    "soda_assassin": [
        ["dialogue", "Narrator: You cloak yourself in fizz and vengeance. You hunt corrupted vending machines in the shadows."],
        ["dialogue", "You: Each can I destroy... brings balance."],
        ["dialogue", "Narrator: You become a legend in the Carbonation Underworld."],
        ["cdialogue", "Ending: Fizzblade of Justice"],
        ["play", "main_menu"]
    ],

    "soda_prophet": [
        ["dialogue", "Narrator: You see visions of the Soda Messiah. You begin preaching."],
        ["dialogue", "You: BEHOLD, THE SPIRIT OF PEPSI COMPRESSED!"],
        ["dialogue", "Narrator: You gain followers. You start a cult."],
        ["dialogue", "Narrator: Years later, you're overthrown by a rebellious off-brand orange soda sect."],
        ["cdialogue", "Ending: The Carbonated Crusade"],
        ["play", "main_menu"]
    ],

    "bubbleverse_conqueror": [
        ["dialogue", "Narrator: Armed with infinite carbonation, you invade alternate realities."],
        ["dialogue", "Narrator: You defeat CokeBot Prime. You enslave Earth 72-B."],
        ["dialogue", "Narrator: Eventually, you confront your original self, sipping water."],
        ["dialogue", "You: Weak."],
        ["cdialogue", "Ending: Supreme Lord of Bubbles"],
        ["play", "main_menu"]
    ],
}

if 'specials' in globals():
    for scene, parts in specials.items():
        scenes[scene] = parts

