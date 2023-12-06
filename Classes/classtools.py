class AttrDisplay:
    """
    Предоставляет наследуемый метод перегрузки отображения, который показывает
экземпляры c их именами классов и пары имя=значение для каждого атрибута,
сохраненного в самом экземпляре (но не атрибутов, унаследованных от his классов) .
Может соединяться c любым классом и будет работать на любом экземпляре.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
    
if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
            

    class SubTest(TopTest):
        pass
    
