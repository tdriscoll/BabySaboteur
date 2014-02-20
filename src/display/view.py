from PyQt4.QtGui import QGraphicsView, QPushButton, QGraphicsScene, QGraphicsSimpleTextItem, qApp, QBrush, QColor, QFont
from PyQt4.QtCore import  QRectF, Qt
from functools import partial 
from utility.string_utility import make_pretty

class View(QGraphicsView):
    
    TEXT_COLOR = QColor(1,1,1)
    BOLDISH = QFont("Times", 30, QFont.Bold)
    NORMALISH = QFont("Times", 30, QFont.Normal)
    
    def __init__(self):
        QGraphicsView.__init__(self)
        self.resize(1024, 768) 
        self.qtscene = None
        self.references = []
    
    def display_question(self, question, answers, selected_index = None, correct = None):
        self._init_scene()
        x = 50
        y = 25
        item =  QGraphicsSimpleTextItem(question)
        item.setBrush(self.TEXT_COLOR)
        item.setFont(self.BOLDISH) 
        item.setX(x)
        item.setY(y)
        self.qtscene.addItem(item)
        self.references.append(item)
        y += 75
        
        for index, answer in enumerate(answers):
            index += 1
            item =  QGraphicsSimpleTextItem("%s) %s" % (index, answer))
            item.setBrush(self.TEXT_COLOR)
            item.setFont(self.NORMALISH) 
            item.setX(x)
            item.setY(y)
            item.setAcceptHoverEvents(True)
            self.qtscene.addItem(item)
            self.references.append(item)
            #TODO: do not register click but do show check or not
            if not selected_index:
                item.hoverEnterEvent = partial(self.on_hover_answer, item) 
                item.hoverLeaveEvent = partial(self.on_unhover_answer, item) 
                item.mousePressEvent = partial(self.on_click_answer, index) 
            elif selected_index == index:
                if correct:
                    item =  QGraphicsSimpleTextItem(u"\u2713")
                    item.setBrush(QBrush(QColor(0,150,0)))
                    item.setX(0)
                else:
                    item =  QGraphicsSimpleTextItem("X")
                    item.setBrush(QBrush(QColor(255,0,0)))
                    item.setX(3)
                item.setFont(self.BOLDISH)
                item.setY(y)
                self.qtscene.addItem(item)
                self.references.append(item)
                
            y += 50
        return x, y
    
    def display_answer(self, question, answers, correct_answer, description, selected_index, correct):
        x, y = self.display_question(question, answers, selected_index, correct) #TODO pass what to check and if right or wrong
        y += 50
        item =  QGraphicsSimpleTextItem("Correct Answer: %s" % correct_answer)
        item.setBrush(self.TEXT_COLOR)
        font = QFont(self.BOLDISH)
        font.setUnderline(True)
        item.setFont(font) 
        item.setX(x)
        item.setY(y)
        self.qtscene.addItem(item)
        self.references.append(item)
        
        y += 60
        item =  QGraphicsSimpleTextItem(make_pretty(description, 55))
        item.setBrush(self.TEXT_COLOR)
        item.setFont(self.NORMALISH) 
        item.setX(x)
        item.setY(y)
        self.qtscene.addItem(item)
        self.references.append(item)
        
        item = QPushButton('Next')
        item.clicked.connect(self.on_next)
        item.setFont(self.BOLDISH) 
        item.move(x+700, y)
        self.qtscene.addWidget(item)
        self.references.append(item)
        
    
    def _init_scene(self):
        self.qtscene = QGraphicsScene(self)
        self.qtscene.setSceneRect(QRectF(0, 0, 1000, 750))
        brush = QBrush(QColor(240,245,250))
        self.qtscene.setBackgroundBrush(brush)
        self.setScene(self.qtscene)
        self.references = []
    
    def on_next(self, event):
        self.next()
    
    def on_hover_answer(self, item, event):
        item.setBrush(QBrush(QColor(100,1,1)))
    
    def on_unhover_answer(self, item, event):
        item.setBrush(self.TEXT_COLOR)
        
    def on_click_answer(self, answer_index, event):
        self.select_answer(answer_index)
    
    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key_Escape:
            self.quit()
        
    def quit(self):
        qApp.quit() 
        
