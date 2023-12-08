# Author : Abigail Leppo
# Class : ITN160
# Class Section : 201
# Date : 12/01/2023
# Assignment : Unit 3 Final Project
import kiosk
from guizero import App, Text

app = App(title='Beachside Restaurant', height=100, width=300, bg='azure')
menu = []
order = {}
order_amount = {}
accumulator = 0.00
total = 'Your total will be ' + '$' + str(accumulator)
subtotals = []
text_box = Text(app, text='Welcome to the Beach Restaurant!')
text_box = Text(app, text= '')
toptext = Text(app, text='Menu:')
fillertext2 = Text(app, text= '')

with open('menu.csv') as kiosk_file:
    reader = kiosk.reader(kiosk_file)
    for row in reader:
        kiosk.append([row[0], row[1], float(row[2]), row[3]])
        kioskvar = []
        order.update({row[0]: row[1:]})
        order_amount.update({row[0]: 0})
    for index, menu_item in enumerate(menu):
        menutext = 'menu_text'.format(index)
        vars()[menutext] = Text(app, text= '{:2} {:2} Price: ${:2.2f} Description: {:2}' .format(menu_item[0], menu_item[1], menu_item[2], menu_item[3]))
    menudis = Text(app, text)
    text = Text(app, text='Input order # below:')
    orderbox = TextBox(app)
    text2 = Text(app, text='And how many you want:')
    quantitybox = TextBox(app, text = '1')
    fillertext3 = Text(app, text= '')
    selection = ''
    def ordering():
        global accumulator
        selection = orderbox.value
        if selection not in order or quantitybox.value == int(0) or quantitybox.value == '':
            text3 = Text(app, text= 'Please enter a valid item or amount of items')
        else:
            quantity = int(quantitybox.value)
            order_amount[selection] += int(quantity)
            accumulator += float(order[selection][1]) * float(quantity)
            subtotal = order[selection] + [quantity, order[selection][1] * int(quantity)]
            subtotals.append(subtotal)
    order_button = PushButton(app, text='Order', command=ordering)
    def done():
        menudis.hide()
        order_button.hide()
        orderbox.hide()
        quantitybox.hide()
        done_button.hide()
        text.value = ''
        text2.value = ''
        endtotal = 'Your total will be ' + '$' + str(accumulator)
        totaltext = Text(app, text=endtotal)
        subtotal = Text(app, text='Subtotals:')
        for index, subtotals_item in enumerate(subtotals):
            subtotaltext = 'subtotal_text'.format(index)
            vars()[subtotaltext] = Text(app, text='{:2} x{}   ${:5}'.format(subtotals_item[0], subtotals_item[3], subtotals_item[1]))
    done_button = PushButton(app, text='Done Ordering', command=done)
app.display()