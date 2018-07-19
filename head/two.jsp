<%@ page contentType="text/html;charset=utf-8"%>
<head>
    <jsp:include page="head.jsp"/>
</head>
<html>
    <body bgcolor=yellow>
        <P><font size=2 color=blue>This is two.jsp</font>
        <font size=3>
            <% String s=request.getParameter("number");
            out.println("<br>传递过来的值是"+s);
            int i=Integer.parseInt(s);
            s=String.valueOf((i+30)%70);
            %>
            <br><img src ="a.jpg" width="<%=s%>" height="<%=s%>"></img>
        </font>
    </body>
</html> 
