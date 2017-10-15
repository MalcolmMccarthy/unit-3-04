#
#
#
#
import ui
def check_button_touch_up_inside(sender):
    year_entered = int(view['year_textfield'].text)
    
    if (year_entered % 4) == 0:
        if (year_entered % 100) == 0:
            if (year_entered % 400) == 0:
            	view['answer_label'].text = 'It is a leap year'
            else:
              view['answer_label'].text = 'Not a leap year'
        else:
          view['answer_label'].text = 'Not a leap year'
    else:
    	view['answer_label'].text = 'Not a leap year'

view = ui.load_view()
view.present('sheet')
